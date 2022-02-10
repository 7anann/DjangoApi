
from rest_framework import serializers
from .models import myuser, Project


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = myuser
        exclude = ['fb_account', 'birthdate', 'country', 'is_active']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields=('title','details','category','totalTarget','start_date','end_date','tags','image')