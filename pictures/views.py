import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from pictures.models import Event, Picture


def list_events(request):
    events = Event.objects.all()
    data = {'events': events}
    return render(request, 'event_list.html', data)


def list_pictures(request):
    pictures = Picture.objects.all()
    data = {'events': pictures}
    return render(request, 'event_list.html', data)


def index(request):
    events = Event.objects.all().order_by('date').reverse()
    #todo add photo data
    data = {'events': events}
    return render(request, 'index.html', data)


def event(request, event_id):
    name = Event.objects.filter(id=event_id)[0]
    pictures = Picture.objects.filter(event_id=event_id)
    data = {
        'time': name.description_text,
        'pictures': pictures,
        'event_id': event_id
    }
    return render(request, 'event_page.html', data)


def eventqr(request, event_id):
    # print(request.path.replace("/qr", ''))
    data = {
        "qr": "this is an event qr",
        "path": request.path.replace("/qr", '')
    }
    return render(request, 'event_qr.html', data)
