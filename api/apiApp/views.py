from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = myuser.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]
    
    
class loginView(APIView):
    serializer_class = Login

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = Login(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

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