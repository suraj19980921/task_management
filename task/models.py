from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status_choices = [
        ('Todo', 'Todo'),
        ('Inprogress', 'Inprogress'),
        ('Done', 'Done'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Todo')

class TaskMember(models.Model):
    task = models.ForeignKey(Task, related_name='members', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
