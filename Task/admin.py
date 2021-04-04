from django.contrib import admin
from .models import TaskType, Task

# Register your models here.

admin.site.register(TaskType)
admin.site.register(Task)