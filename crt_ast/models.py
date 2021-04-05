from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator
#from Asset_Life_Cycle.models import LifeCyclePhase


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
    office_location = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self, *args, **kwargs):
        return "{} {}".format(self.department, self.office_location)

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # connect to django user 
    office_info = models.ForeignKey(Office, on_delete=models.CASCADE)
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
    lc_phase = models.ForeignKey("Asset_Life_Cycle.LifeCyclePhase", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    # BaseSpatialField.srid()
    geom = models.GeometryField()
    elevation = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(blank=True, null=True, upload_to='asset_photo/')
    comissioning_date = models.DateField(null=True, blank=True)
    decommission_date = models.DateField(null=True, blank=True)

    active_choices = (('Yes', "Active"), ('No', "Inactive"),
                      ('Maintenance', "Maintenance"))
    active = models.CharField(max_length=11,
                              choices=active_choices, null=True, blank=True)

    description = models.CharField(max_length=256, null=True, blank=True)

    markersize= models.CharField(max_length=7, null=True)
    markercolor = models.CharField(max_length=7, null=True)
    markersymbol = models.CharField(max_length=15, null=True) 


    def __str__(self, *args, **kwargs):
        return "{}, Type: {}".format(self.name, self.type.name)

class AssetPropertyValue(models.Model):
    property = models.ForeignKey(AssetTypeProperty, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    value = models.CharField(max_length=256)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self, *args, **kwargs):
        return "Type: {}, Property: {}, Value: {}".format(self.asset.name, self.property.name, self.value)
