from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "frontend/index.html", context={"homepage": True})


def about(request):
    return render(request, "frontend/about.html")


def activities(request):
    return render(request, "frontend/activities.html")


def attractions(request):
    return render(request, "frontend/attractions.html")


def contact_us(request):
    return render(request, "frontend/contact-us.html")


def excursions(request):
    return render(request, "frontend/excursions.html")


def gallery(request):
    return render(request, "frontend/gallery.html")


def reservation(request):
    return render(request, "frontend/reservation.html")


def room_chari_deluxe(request):
    return render(request, "frontend/rooms/chari-deluxe.html")


def room_family_deluxe(request):
    return render(request, "frontend/rooms/family-deluxe.html")
