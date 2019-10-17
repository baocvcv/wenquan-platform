""" Populate the database with fake users """
from django.conf import settings
import WenQuan_Platform.settings as app_settings

settings.configure(INSTALLED_APPS=app_settings.INSTALLED_APPS,DATABASES=app_settings.DATABASES)

import django
django.setup()

from backend.models import UserPermissions
from backend.models import User
from backend.models import Profile

def createUser(
    username,
    password="11111111",
    email="a@b.com",
    user_group=User.STUDENT,
    is_banned=False,):
    """ create user"""
    permission = UserPermissions.objects.get(group_name=user_group)
    profile = Profile.objects.create(
        school_name='THU',
    )
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        user_group=user_group,
        user_permissions=permission,
        profile=profile,
        is_banned=is_banned,
    )
    return user

createUser(username="cyx")
createUser(username="bh", is_banned=True)
createUser(username="ydf", user_group=User.ADMIN)
createUser(username='kxz', user_group=User.ADMIN)
createUser(username='xq', user_group=User.SUPER_ADMIN)