from django.db import models

class Song(models.Model):
    name  = models.CharField(max_length=50)
    duration_in_minute = models.IntegerField()
