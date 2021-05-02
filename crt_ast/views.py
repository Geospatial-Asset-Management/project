import django_tables2 as tables
from django.shortcuts import render
from django_tables2 import SingleTableView
from .models import Asset





class AssetTable(tables.Table):
    class Meta :
        model = Asset
        fields = ("type",)

class AssetListView(SingleTableView):
    model = Asset
    table_class = AssetTable
    template_name = 'deneme.html'