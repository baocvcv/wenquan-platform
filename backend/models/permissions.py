""" Permission matrix """
from django.db import models

class UserPermissions(models.Model):
    """ Permissions on user models """
    group_name = models.CharField(max_length=20, primary_key=True)

    view_students = models.BooleanField(default=False)
    create_students = models.BooleanField(default=False)
    ban_students = models.BooleanField(default=False)

    view_admins = models.BooleanField(default=False)
    create_admins = models.BooleanField(default=False)
    ban_admins = models.BooleanField(default=False)

    change_user_group = models.BooleanField(default=False)
