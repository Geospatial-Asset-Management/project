from django.contrib import admin

from .models import AssetType, AssetTypeProperty, AssetPropertyValue, AssetTypeSymbol, Office, Staff, Asset, Point
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget

admin.site.register(AssetType)
admin.site.register(AssetTypeProperty)
admin.site.register(AssetPropertyValue)
admin.site.register(AssetTypeSymbol)
admin.site.register(Office)
admin.site.register(Staff)
admin.site.register(Asset)
admin.site.register(Point)

# Register your models here.


class CityAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }