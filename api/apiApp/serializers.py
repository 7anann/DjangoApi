
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
        
    def create(self, validated_data):
        user = myuser.objects.create(
            Email=validated_data['Email'],
            password=validated_data['password'],
        )

        return user
    class Meta:
        model = myuser
        exclude = ['fb_account', 'birthdate', 'country', 'is_active']

class Login(serializers.HyperlinkedModelSerializer):
    #user = UserSerializer()
    class Meta:
        model = myuser
        fields = ('Email', 'password')

    def validate(self, data):  # validated_data
        email = data.get('Email')
        passw = data.get('password')
        user = myuser.objects.filter(Email=email, password=passw).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Invalid Email address or password")

        return user_obj


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('user','title', 'details', 'category', 'totalTarget',
                  'start_date', 'end_date', 'tags', 'image')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ('name',)


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectTage
        fields = ('tage',)
