from django.db import models
from datetime import datetime

# Create your models here.


class myuser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20, null=True)
    phone_number = models.CharField(max_length=11)
    profile_picture = models.ImageField(
        upload_to='images/', default='images/images.jpeg')
    is_active = models.BooleanField(default=False)
    country = models.CharField(max_length=20, null=True)
    birthdate = models.DateField(null=True)
    fb_account = models.URLField(null=True)

    def __str__(self):
        return self.Email


class Categories(models.Model):
    name = models.CharField(max_length=100)

    def project(self):
        return self.project_set.all()

    def __str__(self):
        return self.name


class ProjectTage(models.Model):
    tage = models.CharField(max_length=100, unique=True)

    def project_all(self):
        return self.project_set.all()

    def __str__(self):
        return self.tage


class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    totalTarget = models.IntegerField()
    tags = models.ManyToManyField(ProjectTage, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(myuser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', default='None/no-img.jpg')

    def getTages(self):
        return self.tags.all()

    def get_date(self):
        time = datetime.now()
        if self.created_at.day == time.day:
            return str(time.hour - self.created_at.hour) + " hours ago"
        if self.created_at.month == time.month:
            return str(time.day - self.created_at.day) + " days ago"
        else:
            if self.created_at.year == time.year:
                return str(time.month - self.created_at.month) + " months ago"

        return self.created_at

    def __str__(self):
        return self.title
