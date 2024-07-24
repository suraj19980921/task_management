from django.contrib import admin
from .models import Task, TaskMember
# Register your models here.

admin.site.register(Task)
admin.site.register(TaskMember)