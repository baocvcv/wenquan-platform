""" Populate the database with fake users """
from django.conf import settings
import WenQuan_Platform.settings as app_settings

settings.configure(INSTALLED_APPS=app_settings.INSTALLED_APPS,DATABASES=app_settings.DATABASES)

import django
django.setup()

from backend.models import UserPermissions
from backend.models import User

groups = UserPermissions.objects.all()
for group in groups:
    group.delete()

UserPermissions.objects.create(
    group_name="Student",
)

UserPermissions.objects.create(
    group_name="Admin",
    view_students=True,
    create_students=True,
    edit_students=True,
    ban_students=True,
)

UserPermissions.objects.create(
    group_name="SuperAdmin",
    view_students=True,
    create_students=True,
    edit_students=True,
    ban_students=True,
    promote_students=True,
    view_admins=True,
    create_admins=True,
    edit_admins=True,
    ban_admins=True,
)
