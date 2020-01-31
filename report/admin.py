from django.contrib import admin
from .models import Incidence,Counties
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ['name','location']

class CountiesAdmin(LeafletGeoAdmin):
    list_display = ['region','name']

admin.site.register(Incidence,IncidenceAdmin)
admin.site.register(Counties,CountiesAdmin)