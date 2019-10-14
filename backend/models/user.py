""" Base model for User """
from django.db import models
from django.contrib.auth.models import AbstractUser
from .permissions import UserPermissions
from .profile import Profile

class User(AbstractUser):
    """ Extending AbstractUser to create custom User

    Attributes:
    """
    STUDENT = 'ST'
    ADMIN = 'AD'
    SUPER_ADMIN = 'SA'
    USER_GROUP_CHOICES = [
        ('ST', 'Student'),
        ('AD', 'Admin'),
        ('SA', 'SuperAdmin'),
    ]
    user_group = models.CharField(
        max_length=2,
        choices=USER_GROUP_CHOICES,
        default=STUDENT,
    )
    user_permissions = models.ForeignKey(UserPermissions, on_delete=models.CASCADE)
    is_banned = models.BooleanField(default=False)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        "Stringify"
        return self.username + "(%s)" % self.email
