from django.shortcuts import render
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyA7DsJI3ri1eXlyu8wyBfooWw4FZVNmafc')

"""
place_result = gmaps.places('nairobi')
print(place_result)

sample url >> https://maps.googleapis.com/maps/api/geocode/json?address=uhuru+park&key=AIzaSyA7DsJI3ri1eXlyu8wyBfooWw4FZVNmafc
"""
geo_result = gmaps.geocode('uhuru park')
geometry = geo_result[0]['geometry']
location = geometry['location']
lat = location.get('lat')
lng = location.get('lng')
print(lat, lng)
# Create your views here.
def home(request):
    test = "Working!"
    content = {
        "test": test
    }
    return render(request, 'home.html', content)
