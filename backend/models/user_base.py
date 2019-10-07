""" Base model for User """
from django.db import models
from django.contrib.auth.models import User

class UserBase(models.Model):
    """ Base class of Users

    Attributes:
        @param user_id
        @param username
        @param email
        @param password
        @param user_type
    """
    # link to the default user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional params
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=1000)
    user_icon = models.CharField(max_length=254)
    register_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        "Stringify"
        return self.username + "(%s)" % self.email

class Admin(UserBase):
    """ General administrators of the site

    Attributes:
    """

    pass


class SuperAdmin(Admin):
    """ Super admin

    """

    pass

class Student(UserBase):
    """ Student users

    Attributes:
    school_name: name of the school

    is_activated:
    """
    
    school_name = models.CharField(max_length=100)

    is_activated = models.BooleanField(default=False)
    #TODO: define Tiku and possible intermediaries
    #authorizations = models.ManyToManyField(Tiku)
