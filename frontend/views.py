from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def activities(request):
    return render(request, "activities.html")


def attractions(request):
    return render(request, "attractions.html")


def contact_us(request):
    return render(request, "contact-us.html")


def excursions(request):
    return render(request, "excursions.html")


def gallery(request):
    return render(request, "gallery.html")


def reservation(request):
    return render(request, "reservation.html")
