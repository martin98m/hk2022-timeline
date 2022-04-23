from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=20)
    description_text = models.CharField(max_length=200)
    date = models.DateTimeField()


class Picture(models.Model):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=200)
