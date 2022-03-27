from django.contrib import admin
from . models import Pic, Category, Location 

# Register your models here.
admin.site.register(Pic)
admin.site.register(Category)
admin.site.register(Location)