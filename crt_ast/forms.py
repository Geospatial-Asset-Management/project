from django import forms
from .models import Asset
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget


class AssetForm(forms.ModelForm):
    class Meta :
        model = Asset
        fields = ["type","name","elevation","lc_phase","comissioning_date","decommission_date","active","description","markersize","markercolor","markersymbol"]
 
