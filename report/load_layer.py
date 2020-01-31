import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties

counties_mapping = {
    'region': 'REGION',
    'division': 'DIVISION',
    'statefp': 'STATEFP',
    'statens': 'STATENS',
    'geoid': 'GEOID',
    'stusps': 'STUSPS',
    'name': 'NAME',
    'lsad': 'LSAD',
    'mtfcc': 'MTFCC',
    'funcstat': 'FUNCSTAT',
    'aland': 'ALAND',
    'awater': 'AWATER',
    'intptlat': 'INTPTLAT',
    'intptlon': 'INTPTLON',
    'geom': 'MULTIPOLYGON',
}


county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data\counties.shp'))

def run(verbose=True):
    lm = LayerMapping(Counties, county_shp, counties_mapping,transform=False,encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)