from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TaskType(models.Model):
    asset_type = models.ForeignKey("crt_ast.AssetType", on_delete=models.CASCADE)
    lc_phase = models.ForeignKey("Asset_Life_Cycle.LifeCyclePhase", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self, *args, **kwargs):
    	return self.name

class Task(models.Model):
    task_type = models.ForeignKey("crt_ast.AssetType", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    assigned_by = models.OneToOneField(User, on_delete=models.CASCADE,related_name='assigned_by')
    assigned_to = models.OneToOneField(User, on_delete=models.CASCADE, related_name='assigned_to')
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self, *args, **kwargs):
    	return self.name