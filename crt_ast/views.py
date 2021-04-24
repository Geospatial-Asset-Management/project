from django.views.generic import ListView
from .models import Asset

class AssetListView(ListView):
    model = Asset
    template_name = 'deneme.html'
