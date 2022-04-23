"""timeline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path

import pictures.views
from timeline import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pictures.views.index),
    path('events', pictures.views.list_events),
    path('pictures', pictures.views.list_pictures),

    path('event/<str:event_id>', pictures.views.event),
    path('event/<str:event_id>/qr', pictures.views.eventqr, name='qr'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
