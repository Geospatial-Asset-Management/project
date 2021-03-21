from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
from geojson import Feature, Point, FeatureCollection
from django.template import loader


from crt_ast.models import Asset
from django.core.serializers import serialize
import json


def cesiumAsset(request):
	geojs = serialize('geojson', Asset.objects.all(),
	          geometry_field='geom',
	          fields=('name', ))

	results = json.loads(geojs)

	return HttpResponse(str(results))

"""
def cesiumAsset(request):
    
    assets = []
    
    
    for i in Asset.objects.all():

        f = Feature(geometry=Point((i.lon, i.lat)))
        f['name']=i.Adi
        f['properties']["title"]= i.Adi
        f['properties']["marker-symbol"]= getMarkerSymbol(i.Adi) 
        f['properties']["marker-color"]= "#FF0000"
        
        features.append(f)

    feature_collection = FeatureCollection(features)
    
    return HttpResponse(str(feature_collection))

"""