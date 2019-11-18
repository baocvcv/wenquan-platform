"""Define the model of File"""
from django.db import models


class ImageModel(models.Model):
    """The file instance"""
    image = models.ImageField(upload_to='pictures/', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30, blank=True, null=True)
