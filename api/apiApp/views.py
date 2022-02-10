from django.shortcuts import render
from .models import myuser, Project
from rest_framework import viewsets
from .serializers import UserSerializer, ProjectSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = myuser.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer