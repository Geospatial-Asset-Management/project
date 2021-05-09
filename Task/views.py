from django.shortcuts import render
from .models import Task
import django_tables2 as tables





class TaskTable(tables.Table):
    class Meta :
        attrs = {'class':'table table-striped table-hover'}
        model = Task
        fields = ("task_type","name","description")

# Create your views here.
