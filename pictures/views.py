import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from pictures.models import Event


def index(request):
    now = datetime.datetime.now()
    data = {'time': now}
    return render(request, 'index.html', data)


def list_events(request):
    events = Event.objects.all()
    data = {'events': events}
    return render(request, 'event_list.html', data)


def event(request, eventid):
    name = Event.objects.filter(id=eventid)[0]

    data = {'time': name.description_text}
    return render(request, 'index.html', data)
