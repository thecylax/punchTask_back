from django.contrib.auth.models import User
from rest_framework import viewsets

from punchTaskApp.api.serializers import UserSerializer, TaskSerializer
from punchTaskApp.tasks.models import Task

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
