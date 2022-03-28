from django.conf.urls import url 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('',views.welcome,name='welcome'),
    url('search/',views.get_category,name='get_category'),
    url('location/<str:search_location>/',views.get_location,name='location'),
    url('photos/',views.get_image,name='get_image'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)