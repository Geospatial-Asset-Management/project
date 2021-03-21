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