from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
from geojson import Feature, Point, FeatureCollection, GeometryCollection
from django.template import loader


from crt_ast.models import Asset, Point
from django.core.serializers import serialize

from geo.czmledit import czml
from PIL import ImageColor

from geo.coordConvert import geodetic_to_geocentric

def czmlPoint(request):

    doc1 = czml.CZML()

    packet1 = czml.CZMLPacket(id='document',name="billboards",version='1.0')
    doc1.packets.append(packet1)

    #billboard
    for i in Point.objects.all():

        packet2 = czml.CZMLPacket(id='bb_'+ str(i), name=i.name, status=i.status)

        descri = czml.Description()
        descri.string = i.description
        packet2.description = descri

        bb = czml.Billboard(scale=i.markersize, show=True)

        a = (i.symbol).split("/")
        a = a[-1]


        bb.image ="/static/Cesium/Build/Cesium/Assets/Textures/maki/" + a , #print("pinBuilder.fromMakiIconId('hospital', Cesium.Color.RED, 48)")  # 
        bb.heightReference = "CLAMP_TO_GROUND"
        bb.clampToGround = True

        rgb = ImageColor.getcolor(i.markercolor, "RGB")
        L1=list(rgb)
        if i.status == "Inactive":
            L1.append(127)
        else:
            L1.append(255)
        
        rgb=tuple(L1)

        bb.color = {'rgba': rgb} #i.markercolor

        packet2.billboard = bb

        poz = czml.Position()
        WGS84 = 6378137, 298.257223563
        poz.cartesian = geodetic_to_geocentric(WGS84, i.lat, i.lon, i.height)

        packet2.position = poz

        doc1.packets.append(packet2)


    myczml= doc1.dumps()

    return HttpResponse(str(myczml))

    #return HttpResponse('[ { "id": "document", "name": "CZML Points", "version": "1.0", }, '+ str(points) + "]")

def cesiumAsset(request):
    geojs = serialize('geojson', Asset.objects.all(),
              geometry_field='geom',
              fields=('name', 'description', 'markercolor', 'markersymbol', 'markersize','active'))

    #results = json.loads(geojs)

    return HttpResponse(str(geojs))


"""
def s_cesiumAsset(request):
    
    features = []
    
    
    for i in Asset.objects.all():
        f = Feature(geometry=Point((i.lon, i.lat, i.alti)))
        f["id"]=i.id
        f['name']=i.name
        f['properties']["title"]= i.name
        f['properties']["markersymbol"]= i.markersymbol
        f['properties']["markercolor"]= i.markercolor
        
        features.append(f)
        
    feature_collection = FeatureCollection(features)
    
    return HttpResponse(str(feature_collection))

"""

