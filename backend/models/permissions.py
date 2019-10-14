""" Permission matrix """
from django.db import models

class UserPermissions(models.Model):
    """ Permissions on user models """
    group_name = models.CharField(max_length=20, primary_key=True)

    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    can_view_students = models.BooleanField(default=False)
    can_edit_students = models.BooleanField(default=False)
    can_view_admins = models.BooleanField(default=False)
    can_edit_admins = models.BooleanField(default=False)
