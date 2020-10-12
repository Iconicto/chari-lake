from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('activities', views.activities, name='activities'),
    path('attractions', views.attractions, name='attractions'),
    path('contact', views.contact_us, name='contact_us'),
    path('excursions', views.excursions, name='excursions'),
    path('gallery', views.gallery, name='gallery'),
    path('reservation', views.reservation, name='reservation'),
    path('rooms/chari-deluxe', views.room_chari_deluxe, name='room_chari_deluxe'),
    path('rooms/family-deluxe', views.room_family_deluxe, name='rooms_family_deluxe'),
]
