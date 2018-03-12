from django.shortcuts import render
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyA7DsJI3ri1eXlyu8wyBfooWw4FZVNmafc')

# Create your views here.
def home(request):
    test = "Working!"
    content = {
        "test": test
    }
    return render(request, 'home.html', content)
