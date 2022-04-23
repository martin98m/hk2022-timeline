from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=20)
    description_text = models.CharField(max_length=200)
    date = models.DateTimeField()


class Picture(models.Model):
    image = models.ImageField(null=True, upload_to='images')
    event_id = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=200)
