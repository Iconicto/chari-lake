import requests
from django.shortcuts import render
import os
from django.conf import settings

from frontend.helpers import create_email


def home(request):
    return render(request, "frontend/index.html", context={"homepage": True})


def about(request):
    return render(request, "frontend/about.html")


def activities(request):
    return render(request, "frontend/activities.html")


def attractions(request):
    return render(request, "frontend/attractions.html")


def contact_us(request):
    if request.method == 'POST':
        try:
            resp = requests.post(
                "https://api.mailgun.net/v3/iconicto.com/messages",
                auth=("api", settings.MAILGUN_API_KEY),
                data={"from": "Iconicto Postmaster <postman@iconicto.com>",
                      "to": "info@charilakehotel.lk",
                      "subject": "New client inquiry via charilakehotel.lk",
                      "text": create_email(request.POST)
                      })
            if resp.status_code == 200:
                return render(request, "frontend/contact-us.html",
                              context={"messages": [{"level": "is-success",
                                                     "content": "Your inquiry was routed to management, We will reach back to you as soon as possible"}]})
            else:
                print(resp.text)
                raise Exception(resp.text)
        except:
            return render(request, "frontend/contact-us.html",
                          context={"messages": [{"level": "is-danger",
                                                 "content": "Something went wrong, Try resubmitting or send a direct email to info@charilakehotel.lk"}]})
    else:
        return render(request, "frontend/contact-us.html")


def excursions(request):
    return render(request, "frontend/excursions.html")


def gallery(request):
    images = os.listdir("static/img/gallery")
    return render(request, "frontend/gallery.html", context={"images": sorted(images)})


def rooms(request):
    return render(request, "frontend/rooms.html")


def room_chari_deluxe(request):
    return render(request, "frontend/rooms/chari-deluxe.html")


def room_family_deluxe(request):
    return render(request, "frontend/rooms/family-deluxe.html")


def room_chari_luxury(request):
    return render(request, "frontend/rooms/chari-luxury.html")
