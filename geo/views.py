from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
from geojson import Feature, Point, FeatureCollection, GeometryCollection
from django.template import loader


from crt_ast.models import Asset
from django.core.serializers import serialize
import json


def cesiumAsset(request):
	geojs = serialize('geojson', Asset.objects.all(),
	          geometry_field='geom',
	          fields=('name', 'markercolor', 'markersymbol', ))

	results = json.loads(geojs)

	return HttpResponse(str(geojs))

"""
def s_cesiumAsset(request):
    
    features = []
    
    
    for i in Asset.objects.all():
        f = Feature(geometry=Point((i.lon, i.lat)))
        f['name']=i.name
        f['properties']["title"]= i.name
        f['properties']["markersymbol"]= i.markersymbol
        f['properties']["markercolor"]= i.markercolor
        
        features.append(f)
        
    feature_collection = FeatureCollection(features)
    
    return HttpResponse(str(feature_collection))
"""