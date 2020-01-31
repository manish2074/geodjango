from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
# Create your models here.
class Incidence(models.Model):
    name = models.CharField(max_length=30)
    location = models.PointField(srid=4326)
    object = GeoManager()

    def __str__(self):
        return self.name

class Counties(models.Model):
    region = models.CharField(max_length=2)
    division = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2)
    statens = models.CharField(max_length=8)
    geoid = models.CharField(max_length=2)
    stusps = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    funcstat = models.CharField(max_length=1)
    aland = models.BigIntegerField()
    awater = models.BigIntegerField()
    intptlat = models.CharField(max_length=11)
    intptlon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name