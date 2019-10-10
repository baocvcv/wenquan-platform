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
import hashlib

def createUser(
    username,
    password,
    email,
    is_student=True,
    is_admin=False,
    is_superadmin=False):
    user_type = UserType.objects.create(
        is_student=is_student,
        is_admin=is_admin,
        is_superadmin=is_superadmin
    )
    """ create user"""
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    return User.objects.create_user(
        user_type=user_type,
        username=username,
        password=m.hexdigest(),
        email=email,
    )


def createStudent(
    username="student",
    password="11111111",
    email="cyx@163.com",
    is_banned=False,):
    """ create user"""
    user = createUser(username, password, email)
    return Student.objects.create(
        user=user,
        is_banned=is_banned,
        school_name='Tsinghua'
    )

def createAdmin(
    username="admin",
    password="11111111",
    email="cyx@163.com",):
    """ create user"""
    user = createUser(
        username,
        password,
        email,
        is_student=False,
        is_admin=True,
        is_superadmin=False)
    return Admin.objects.create(
        user=user,
    )

def createSuperAdmin(
    username="admin",
    password="11111111",
    email="cyx@163.com",):
    """ create user"""
    user = createUser(
        username,
        password,
        email,
        is_student=False,
        is_admin=False,
        is_superadmin=True)
    return SuperAdmin.objects.create(
        user=user,
    )

createStudent(username="cyx")
createStudent(username="bh", is_banned=True)
createAdmin(username="ydf")
createAdmin(username='kxz')
createSuperAdmin(username='xq')