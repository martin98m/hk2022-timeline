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
    events = Event.objects.all().order_by('date')
    print(events)
    data = {'events': events}
    return render(request, 'index.html', data)


def event(request, event_id):
    name = Event.objects.filter(id=event_id)[0]
    print('aaaaaaaaaaa')
    pictures = Picture.objects.filter(event_id=event_id)
    data = {
        'time': name.description_text,
        'pictures': pictures}
    return render(request, 'event_page.html', data)


def eventqr(request, event_id):
    print(request.path)
    data = {
        "qr": "this is an event qr",
        "path": request.build_absolute_uri()
    }
    return render(request, 'event_qr.html', data)
