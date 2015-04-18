from django.contrib.auth.models import User
from rest_framework import serializers

from punchTaskApp.tasks.models import Task

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
        
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
#        fields = ('url', 'username', 'email', 'groups')
