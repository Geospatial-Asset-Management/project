from django.db import models
from django.contrib.gis.db import models

# Create your models here.


class AssetType(models.Model):
    name = models.CharField(max_length=30)
    industry = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=256, null=True)

    def save(self, *args, **kwargs):
        if not self.industry:
            self.industry = None
        super(AssetType, self).save(*args, **kwargs)

    def __str__(self, *args, **kwargs):
    	return self.name


class AssetTypeProperty(models.Model):
    type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    dtype = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=256, null=True)


class AssetTypeSymbol(models.Model):
    type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    symbol = models.ImageField(upload_to='symbol_img/')
    description = models.CharField(max_length=256, null=True)

class Office(models.Model):
    department = models.CharField(max_length=75)
    office_location = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    description = models.CharField(max_length=256, null=True)


class SeniorStaff(models.Model):
    office_info = models.ForeignKey(Office, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    surname = models.CharField(max_length=75)
    title = models.CharField(max_length=75)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()


class Staff(models.Model):
    office_info = models.ForeignKey(Office, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    surname = models.CharField(max_length=75)
    title = models.CharField(max_length=75)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    reports_to = models.ForeignKey(SeniorStaff, on_delete=models.CASCADE)


class Asset(models.Model):
    type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    dataEntryStaff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    # BaseSpatialField.srid()
    geom = models.GeometryField()
    elevation = models.IntegerField(null=True)
    photo = models.ImageField(null=True, upload_to='templates/images/asset_photo/')
    comissioning_date = models.DateField(null=True)
    decommission_date = models.DateField(null=True)

    active_choices = (('Yes', "Active"), ('No', "Inactive"),
                      ('Maintenance', "Maintenance"))
    active = models.CharField(max_length=11,
                              choices=active_choices)

    description = models.CharField(max_length=256, null=True)

    #markersymbol = models.CharField(max_length=1, null=True) 
    #markercolor = models.CharField(max_length=7, null=True) 

class AssetPropertyValue(models.Model):
    property = models.ForeignKey(AssetTypeProperty, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=256)
    description = models.CharField(max_length=256, null=True)
