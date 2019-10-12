""" Base model for User """
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserType(models.Model):
    """ Type for users """
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

class User(AbstractUser):
    """ Extending AbstractUser to create custom User

    Attributes:
        @param user_id
        @param username
        @param email
        @param password
        @param user_type
    """
    user_type = models.OneToOneField(UserType, on_delete=models.CASCADE)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        "Stringify"
        return self.username + "(%s)" % self.email

class Admin(models.Model):
    """ General administrators of the site

    Attributes:
    """
    #link to User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class SuperAdmin(models.Model):
    """ Super admin

    """
    #link to User
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Student(models.Model):
    """ Student users

    Attributes:
    school_name: name of the school

    is_activated:
    """
    #link to User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    #need to define Tiku and possible intermediaries
    #authorizations = models.ManyToManyField(Tiku)
