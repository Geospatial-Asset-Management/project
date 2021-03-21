from django.contrib import admin

from .models import AssetType, AssetTypeProperty, AssetPropertyValue, AssetTypeSymbol, Office, Staff, Asset

admin.site.register(AssetType)
admin.site.register(AssetTypeProperty)
admin.site.register(AssetPropertyValue)
admin.site.register(AssetTypeSymbol)
admin.site.register(Office)
admin.site.register(Staff)
admin.site.register(Asset)

# Register your models here.

