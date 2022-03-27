from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Pic, Location, Category

# Create your views here.
def welcome(request):
    image=Pic.objects.all()
    locations = Location.all_Locations()
    return render(request, 'home.html', {'images': Pic, 'locations': Location})
