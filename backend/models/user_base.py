from django.db import models

class UserBase(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
