""" Populate the database with fake users """
from django.conf import settings
import WenQuan_Platform.settings as app_settings
import django

if __name__ == '__main__':
    settings.configure(INSTALLED_APPS=app_settings.INSTALLED_APPS,DATABASES=app_settings.DATABASES)
    django.setup()

from backend.models import User
from backend.models import UserPermissions
from backend.tests.utils import create_permission

groups = UserPermissions.objects.all()
for group in groups:
    group.delete()

create_permission().save()
create_permission("Admin").save()
create_permission("SuperAdmin").save()
