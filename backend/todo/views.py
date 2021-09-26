from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializer, ProjectSerializer
from .models import Task, Project

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()