from django.shortcuts import render
from rest_framework import generics
from rest_framework_mongoengine import viewsets
from .serializers import TaskSerializers
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Task.objects.all()
    serializer_class = TaskSerializers



class CreateTask(generics.CreateAPIView):
    """ module to create a new car instance"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializers