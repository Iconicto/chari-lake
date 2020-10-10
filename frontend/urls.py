from django.urls import path
from django.views.generic.base import RedirectView
from . import views

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('activities', views.activities, name='activities'),
    path('attractions', views.attractions, name='attractions'),
    path('contact', views.contact_us, name='contact_us'),
    path('excursions', views.excursions, name='excursions'),
    path('gallery', views.gallery, name='gallery'),
    path('reservation', views.reservation, name='reservation'),
    path(r'^favicon\.ico$', favicon_view),
]
