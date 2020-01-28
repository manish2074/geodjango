from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

# Create your views here.

longitude = 9498500.6
latitude = 3211500.3223

user_location =Point(longitude, latitude,srid=4326)

class Home(generic.ListView):
    model = Shop
    context_object_name = "shops"
    queryset= Shop.objects.annotate(
        distance=Distance('location',user_location)
    ).order_by('distance')[:6]
    template_name = "shops/index.html"
    