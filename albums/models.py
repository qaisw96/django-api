from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
