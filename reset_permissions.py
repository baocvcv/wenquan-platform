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
    group_name="ST",
    is_student=True,
)

UserPermissions.objects.create(
    group_name="AD",
    is_admin=True,
    can_view_students=True,
    can_edit_students=True,
)

UserPermissions.objects.create(
    group_name="SA",
    is_superadmin=True,
    can_view_students=True,
    can_edit_students=True,
    can_view_admins=True,
    can_edit_admins=True,
)
