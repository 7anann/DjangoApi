from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = myuser.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def get_context_data(self,**kwargs):
        if 'Email' in self.request.session :
             authenticated=myuser.objects.get(Email=self.request.session['Email'])
        else:
            authenticated=None
        context = super().get_context_data(**kwargs)
        context['authenticated'] = authenticated
        return context
    
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)   
     
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    
class TagViewSet(viewsets.ModelViewSet):
    queryset = ProjectTage.objects.all()
    serializer_class = TagSerializer
    
    
        
