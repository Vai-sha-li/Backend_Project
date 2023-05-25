from django.db import models
from events.models import Event

class Nudge(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to='nudge_images/')
    scheduled_on = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    description = models.TextField()
    icon = models.CharField(max_length=255)
    invitation = models.CharField(max_length=255)

    def __str__(self):
        return self.title
