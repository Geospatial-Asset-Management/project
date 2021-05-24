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
        ("#FFFFFF90", "white"),
        ("#00000090", "black"),
        ("#80808090", "grey"),
        ("#FFFF0090", "yellow"),
        ("#FF000090", "red"),
        ("#0000FF90", "blue"),
        ("#00800090", "green"),
        ("#FFA50090", "orange"),
        ("#87CEEB90", "light blue"),
    ]
    color = ColorField(format="hexa", null=True, choices=COLOR_CHOICES, blank=True, default="#FFFFFFFF")

    def __str__(self, *args, **kwargs):
        return self.name