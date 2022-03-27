from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Pic, Location, Category

# Create your views here.
def welcome(request):
    image=Pic.objects.all()
    locations = Location.all_Locations()
    return render(request, 'home.html', {'images': Pic, 'locations': Location})

def get_category(request):
    title = "Category"
    locations = Location.objects.all()

    if 'category' in request.GET and request.GET["category"]:
        search_category=request.GET.get("category")
        searched_category=Pic.search_image(search_category)
        message = f"{search_category}"


        return render(request,'all-gallery/search.html',{'message':message,'images':searched_category,'title':title,'locations':locations})
    else:
        message = "Please enter any category"
        return render(request, 'search.html',{"message":message})