from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/')
    tagline = models.CharField(max_length=255)
    schedule = models.DateTimeField()
    description = models.TextField()
    moderator = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    rigor_rank = models.IntegerField()

    def __str__(self):
        return self.name
