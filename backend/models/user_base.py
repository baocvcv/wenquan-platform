""" Base model for User """
from django.db import models

class UserBase(models.Model):
    """ Base class of Users

    Attributes:
        @param user_id
        @param username
        @param email
        @param password
        @param user_type
    """
    user_id = models.AutoField()
    username = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=256)
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

class Students(UserBase):
    """ Student users
    """
    
    school_name = models.CharField(max_length="100")
    #TODO: define Tiku and possible intermediaries
    #authorizations = models.ManyToManyField(Tiku)
