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
    photos = []
    for e in events:
        img = Picture.objects.filter(event_id=e.id).first()
        if img is None:
            img = Picture.objects.last()
        photos.append(img)
    print(events[0].description_text)

    #todo add photo data
    data = {
        'data': zip(events, photos),
        'datab': zip(events, photos),
        'datac': zip(events, photos),
        'datad': zip(events, photos),
        'photo_count': len(photos)
    }
    return render(request, 'index.html', data)


def event(request, event_id):
    event = Event.objects.filter(id=event_id)[0]
    pictures = Picture.objects.filter(event_id=event_id)
    data = {
        'pictures': pictures,
        'event_id': event_id,
        'event_name': event.name
    }
    return render(request, 'event_page.html', data)


def eventqr(request, event_id):
    data = {
        "path": request.path.replace("/qr", '')
    }
    return render(request, 'event_qr.html', data)
