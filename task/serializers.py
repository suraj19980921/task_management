from rest_framework import serializers
from .models import Task, TaskMember

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'status']

class TaskMemberSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    class Meta:
        model = TaskMember
        fields = ['user_id', 'first_name', 'last_name']
