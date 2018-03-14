"""
We define our app routes here. We import;

1. url - This will allow us to define our url paths using
django's inbuilt url method.
2. views - This allows us to connect a path to the view function rendering it.
3. settings - this allows us to connect the static files to our app.
4. static
"""

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.home, name='home'),
    url('^test/$', views.test, name='test'),
    url('^visualize/$', views.visualize, name='visualize'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
