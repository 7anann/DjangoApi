
from rest_framework import serializers
from .models import myuser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = myuser
        exclude = ['fb_account', 'birthdate', 'country', 'is_active']

