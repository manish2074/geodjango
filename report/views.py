from django.shortcuts import render
from .models import Counties
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name='report/index.html'


def county_datasets(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties,content_type='json')