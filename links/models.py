from django.db import models
from django.conf import settings


# Create your models here.
class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
