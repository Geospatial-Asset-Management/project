from django.db import models
from django.contrib.gis.db import models
from crt_ast.models import AssetType
from colorfield.fields import ColorField

# Create your models here.

class LifeCycle(models.Model):
    asset_type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self, *args, **kwargs):
        return self.name

class LifeCyclePhase(models.Model):
    lc = models.ForeignKey(LifeCycle, on_delete=models.CASCADE)
 #  asset_prop_value_id = models.ForeignKey("crt_ast.AssetPropertyValue", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    COLOR_CHOICES = [
        ("#FFFFFFFF", "white"),
        ("#000000FF", "black"),
        ("#808080FF", "grey"),
        ("#FFFF00FF", "yellow"),
        ("#FF0000FF", "red"),
        ("#0000FFFF", "blue"),
        ("#008000FF", "green"),
        ("#FFC0CBFF", "pink"),
    ]
    color = ColorField(format="hexa", null=True, blank=True, default="#FFFFFFFF") #choices=COLOR_CHOICES

    def __str__(self, *args, **kwargs):
        return self.name