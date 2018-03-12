"""
We define our app routes here. We import;

1. url - This will allow us to define our url paths using django's inbuilt url method.
2. views - This allows us to connect a path to the view function rendering it.

"""

from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.home, name='home'),
]