""" Base model for User """
from django.db import models

class UserBase(models.Model):
    """ Base class of Users

    Attributes:
        @param user_name
        @param email
        @param password
        @param user_type
    """
    user_id = models.AutoField()
    username = models.CharField(max_length=50, primary_key=True)
    email = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        "Stringify"
        return self.username + "(%s)" % self.email
