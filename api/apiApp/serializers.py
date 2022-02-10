
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = myuser
        exclude = ['fb_account', 'birthdate', 'country', 'is_active']


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
