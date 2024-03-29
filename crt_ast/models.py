from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField
from colorfield.fields import ColorField

# Create your models here.


class AssetType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    industry = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self, *args, **kwargs):
        return self.name

class AssetTypeProperty(models.Model):
    type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    dtype = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self, *args, **kwargs):
        return "{}, Type: {}".format(self.name, self.type.name)

class AssetTypeSymbol(models.Model):
    type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    symbol = models.ImageField(upload_to='symbol_img/', unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self, *args, **kwargs):
        return "{}, Type: {}".format(str(self.symbol), self.type.name)

class Office(models.Model):
    department = models.CharField(max_length=75)
    office_location = models.CharField(max_length=100, null=True, blank=True, verbose_name='Office Location')
    email = models.EmailField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self, *args, **kwargs):
        return "{} {}".format(self.department, self.office_location)

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # connect to django user 
    office_info = models.ForeignKey(Office, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Office Info')
    #name = models.ForeignKey(User, on_delete=models.CASCADE)
    #surname = models.CharField(max_length=75)
    title = models.CharField(max_length=75, null=True, blank=True)
    #email = models.EmailField(max_length=100, unique=True)
    phone = models.IntegerField(null=True, blank=True, unique=True, validators=[MaxValueValidator(99999999999999999)])
    #reports_to = models.ForeignKey(SeniorStaff, on_delete=models.CASCADE)

    def __str__(self):  
        return "%s's profile" % self.user  

def create_user_profile(sender, instance, created, **kwargs):  
	
    if created:  
      profile, created = Staff.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 

 #   def __str__(self, *args, **kwargs):
   #    return "{} {}, Job Title: {}".format(self.name, self.surname, self.title)

# for django user auth / email field 
#User._meta.get_field('email')._unique = True
#User._meta.get_field('email').blank = False
#User._meta.get_field('email').null = False


class Asset(models.Model):
    type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    lc_phase = models.ForeignKey("Asset_Life_Cycle.LifeCyclePhase", on_delete=models.CASCADE, verbose_name='Life Cycle Phase')
    name = models.CharField(max_length=30)

    #city = models.CharField(max_length=255)
    geom = models.GeometryField()
    #geom = LocationField(zoom=13, default=Point(32.733820,39.865586), verbose_name='Location')
    elevation = models.IntegerField(null=True, blank=True)

    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    
    photo = models.ImageField(blank=True, null=True, upload_to='asset_photo/')
    comissioning_date = models.DateField(null=True, blank=True , verbose_name='Comissioning Date')
    decommission_date = models.DateField(null=True, blank=True, verbose_name='Decommission Date')

    active_choices = (('Active', "Active"), ('Inactiveive', "Inactive"),
                      ('Maintenance', "Maintenance"))
    active = models.CharField(max_length=11,
                              choices=active_choices, null=True, blank=True)

    description = models.CharField(max_length=256, null=True, blank=True)

    markersize= models.CharField(max_length=7, null=True, blank=True)
    markercolor = models.CharField(max_length=7, null=True, blank=True)
    markersymbol = models.CharField(max_length=15, null=True, blank=True) 


    def __str__(self, *args, **kwargs):
        return "{}, Type: {}".format(self.name, self.type.name)

class Point(models.Model):
    type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    lc_phase = models.ForeignKey("Asset_Life_Cycle.LifeCyclePhase", on_delete=models.CASCADE, verbose_name='Life Cycle Phase')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=256, null=True, blank=True)

    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)

    comissioning_date = models.DateField(null=True, blank=True)
    decommission_date = models.DateField(null=True, blank=True)

    photo = models.ImageField(blank=True, null=True, upload_to='asset_photo/')
    symbol = models.FilePathField(path='crt_ast/static/Cesium/Build/Cesium/Assets/Textures/maki/', null=True, blank=True)
    markersize= models.FloatField(null=True, blank=True, default=0.5)
    COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black"),
        ("#808080", "grey"),
        ("#FFFF00", "yellow"),
        ("#FF0000", "red"),
        ("#0000FF", "blue"),
        ("#008000", "green"),
        ("#FFA500", "orange"),
        ("#87CEEB", "light blue"),
    ]
    markercolor = ColorField(format="hex", null=True, choices=COLOR_CHOICES, blank=True, default="#FFFFFF")


    def __str__(self, *args, **kwargs):
        return "{}, Type: {}".format(self.name, self.type.name)

class polygonn(models.Model):
    type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    lc_phase = models.ForeignKey("Asset_Life_Cycle.LifeCyclePhase", on_delete=models.CASCADE, verbose_name='Life Cycle Phase')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=256, null=True, blank=True)

    geo = models.CharField(max_length=500)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)

    COLOR_CHOICES = [
        ("#FFFFFF90", "white"),
        ("#00000090", "black"),
        ("#80808090", "grey"),
        ("#FFFF0090", "yellow"),
        ("#FF000090", "red"),
        ("#0000FF90", "blue"),
        ("#00800090", "green"),
        ("#FFA50090", "orange"),
        ("#87CEEB", "light blue"),
    ]
    color = ColorField(format="hex", null=True, choices=COLOR_CHOICES, blank=True, default="#FFFFFF")


class AssetPropertyValue(models.Model):
    property = models.ForeignKey(AssetTypeProperty, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    value = models.CharField(max_length=256)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self, *args, **kwargs):
        return "Type: {}, Property: {}, Value: {}".format(self.asset.name, self.property.name, self.value)


    def __str__(self, *args, **kwargs):
        return "{}, Type: {}".format(self.name, self.type.name)
