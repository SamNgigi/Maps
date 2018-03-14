from django.shortcuts import render
import googlemaps
from .models import Location
import datetime as dt
import json
from django.core.serializers.json import DjangoJSONEncoder
"""
Import the serializers to convert the query set into json that we can
parse as javascript vars. 
"""
from django.core import serializers
"""
We use python's googlemap client to make the api request. We pass in the
apikey.
"""

gmaps = googlemaps.Client(key='AIzaSyA7DsJI3ri1eXlyu8wyBfooWw4FZVNmafc')

"""
place_result = gmaps.places('nairobi')
print(place_result)

sample url
>> https://maps.googleapis.com/maps/api/geocode/json?address=uhuru+park&key=AIzaSyA7DsJI3ri1eXlyu8wyBfooWw4FZVNmafc

We then choose the api we want to interact with. In this case it is googlemap's
geocoding api.
The code below does a similar request and the url above
"""


"""
We go through the response we get from the api and get the location coordinates
What we have below is similar to;
latitude = geo_result[0]['geometry']['location'].get('lat'),
longitude = geo_result[0]['geometry']['location'].get('lng'),
"""

# geometry = geo_result[0]['geometry']
# location = geometry['location']
# lat = location.get('lat')
# lng = location.get('lng')
# We print see the response we get.
# print(latitude, longitude)
# Create your views here.


def home(request):
    test = "Working!"
    if 'address' in request.GET and request.GET['address']:
        address = request.GET.get("address")
        # print(query)
        geo_result = gmaps.geocode(address)
        # print(geo_result)
        latitude = geo_result[0]['geometry']['location'].get('lat')
        longitude = geo_result[0]['geometry']['location'].get('lng')
        # print(geo_result)
        location = Location()
        location.name = address
        location.latitude = latitude
        location.longitude = longitude
        location.time = dt.datetime.now()
        location.save()
        content = {
            "test": test,
            "latitude": latitude,
            "longitude": longitude,
        }
        return render(request, 'home.html', content)
    else:
        content = {
            "test": test,
        }
        return render(request, 'home.html', content)


def test(request):
    test = 'working'
    content = {
        "test": test
    }
    return render(request, "test.html", content)


def visualize(request):
    test = "Working!"
    spots = list(Location.objects.all())

    print(spots)
    coords = {"1": 1, "2": 2}
    coords_json = json.dumps(coords, cls=DjangoJSONEncoder)
    spots_json = serializers.serialize('json', spots)
    content = {
        "test": test,
        "coords_json": coords_json,
        "spots_json": spots_json,
    }
    return render(request, 'visualize.html', content, locals)
