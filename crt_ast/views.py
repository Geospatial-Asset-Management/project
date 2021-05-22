import django_tables2 as tables
from django.shortcuts import render
from django_tables2 import SingleTableView
from .models import Asset
from .models import Point
from .forms import AssetForm
from django.shortcuts import render,redirect





class AssetTable(tables.Table):
    class Meta :
        attrs = {'class':'table table-striped table-hover'}
        model = Asset
        fields = ("type","name","lc_phase")

class PointTable(tables.Table):
    class Meta :
        attrs = {'class':'table table-striped table-hover'}
        model = Point
        fields = ("type","name","lc_phase")
     



class AssetListView(SingleTableView):
    model = Asset
    table_class = AssetTable
    template_name = 'deneme.html'
    








def CreateAsset(request):
    form = AssetForm(request.POST or None)
    if form.is_valid():
        form.save()


        return redirect("index")


    return render(request,"crt_asset.html",{"form":form})
