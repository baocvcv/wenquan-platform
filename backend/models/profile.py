""" User Profile """
from django.db import models

class Profile(models.Model):
    """ User profile
    """
    school_name = models.CharField(max_length=100)
