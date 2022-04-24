from django.shortcuts import render
from pictures.models import Event, Picture


def index(request):
    events = Event.objects.all().order_by('date').reverse()
    photos = []
    for e in events:
        img = Picture.objects.filter(event_id=e.id).first()
        if img is None:
            img = Picture.objects.last()
        photos.append(img)

    data = {
        'data': zip(events, photos),
        'datab': zip(events, photos),
        'datac': zip(events, photos),
        'datad': zip(events, photos),
        'photo_count': len(photos)
    }
    return render(request, 'index.html', data)


def event(request, event_id):
    event_by_id = Event.objects.filter(id=event_id)[0]
    pictures = Picture.objects.filter(event_id=event_id)
    data = {
        'pictures': pictures,
        'event_id': event_id,
        'event_name': event_by_id.name
    }
    return render(request, 'event_page.html', data)


def event_qr(request, event_id):
    data = {
        "path": request.path.replace("/qr", '')
    }
    return render(request, 'event_qr.html', data)
