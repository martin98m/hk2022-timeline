from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=30)
    description_text = models.CharField(max_length=300)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.name}, {self.date.strftime('%B-%Y')}"


class Picture(models.Model):
    image = models.ImageField(null=True, upload_to='images')
    event_id = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=300, null=True)
