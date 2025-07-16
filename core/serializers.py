from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = ['title', 'content', 'is_completed', 'due_date', 'user']
