""" Populate the database with fake users """
from django.conf import settings
import WenQuan_Platform.settings as app_settings

settings.configure(INSTALLED_APPS=app_settings.INSTALLED_APPS,DATABASES=app_settings.DATABASES)

import django
django.setup()

from backend.models.user_base import UserType
from backend.models.user_base import User
from backend.models.user_base import Admin
from backend.models.user_base import SuperAdmin
from backend.models.user_base import Student

def createUser(
    username,
    password,
    email,
    is_student=True,
    is_admin=False,
    is_superadmin=False,
    is_banned=False):
    """ create user"""
    user_type = UserType.objects.create(
        is_student=is_student,
        is_admin=is_admin,
        is_superadmin=is_superadmin
    )
    return User.objects.create_user(
        user_type=user_type,
        username=username,
        password=password,
        email=email,
        is_banned=is_banned,
    )


def createStudent(
    username="student",
    password="11111111",
    email="cyx@163.com",
    is_banned=False,):
    """ create user"""
    user = createUser(
        username,
        password,
        email,
        is_banned=is_banned)
    return Student.objects.create(
        user=user,
        school_name='Tsinghua'
    )

def createAdmin(
    username="admin",
    password="11111111",
    email="cyx@163.com",
    is_banned=False,):
    """ create user"""
    user = createUser(
        username,
        password,
        email,
        is_student=False,
        is_admin=True,
        is_superadmin=False,
        is_banned=is_banned)
    return Admin.objects.create(
        user=user,
    )

def createSuperAdmin(
    username="admin",
    password="11111111",
    email="cyx@163.com",
    is_banned=False,):
    """ create user"""
    user = createUser(
        username,
        password,
        email,
        is_student=False,
        is_admin=False,
        is_superadmin=True,
        is_banned=is_banned)
    return SuperAdmin.objects.create(
        user=user,
    )

createStudent(username="cyx")
createStudent(username="bh", is_banned=True)
createAdmin(username="ydf")
createAdmin(username='kxz')
createSuperAdmin(username='xq')