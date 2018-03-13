from django.shortcuts import render
import googlemaps
from datetime import datetime

# We use python's googlemap client to make the api request. We pass in the api key.

gmaps = googlemaps.Client(key='AIzaSyA7DsJI3ri1eXlyu8wyBfooWw4FZVNmafc')

"""
place_result = gmaps.places('nairobi')
print(place_result)

sample url >> https://maps.googleapis.com/maps/api/geocode/json?address=uhuru+park&key=AIzaSyA7DsJI3ri1eXlyu8wyBfooWw4FZVNmafc
"""
# We then choose the api we want to interact with. In this case it is googlemap's geocoding api. The code below does a similar request and the url above
geo_result = gmaps.geocode('uhuru park')
# We go through the response we get from the api and get the location coordinates.
# What we have below is similar to;
# latitude = geo_result[0]['geometry']['location'].get('lat),
# longitude = geo_result[0]['geometry']['location'].get('lng), 
geometry = geo_result[0]['geometry']
location = geometry['location']
lat = location.get('lat')
lng = location.get('lng')
# We print see the response we get.
print(lat, lng)
# Create your views here.
def home(request):
    # We pass in the coordinates we got from our api-call.
    test = "Working!"
    content = {
        "test": test,
        "latitude": lat,
        "longitude":lng,
    }
    return render(request, 'home.html', content)
