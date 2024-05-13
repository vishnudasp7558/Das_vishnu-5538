from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets


# Create your views here.

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CompletedTask(viewsets.ModelViewSet):
    queryset = Task.objects.filter(completed=True)
    serializer_class = TaskSerializer

class NotCompletedTask(viewsets.ModelViewSet):
    queryset = Task.objects.filter(completed=False)
    serializer_class = TaskSerializer