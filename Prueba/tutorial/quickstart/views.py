from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets 
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    """
    Documentacion para la API 
    usuarios editados o vistos
    """
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class=UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer