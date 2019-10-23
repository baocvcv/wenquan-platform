""" Populate the database with fake users """
import django
import WenQuan_Platform.settings as app_settings
from django.conf import settings
from django.utils import timezone

from backend.models import UserPermissions
from backend.models import User
from backend.models import Profile

from backend.models.question_bank import QuestionBank

settings.configure(INSTALLED_APPS=app_settings.INSTALLED_APPS, DATABASES=app_settings.DATABASES)

django.setup()


def createUser(
        username,
        password="11111111",
        email="a@b.com",
        user_group=User.STUDENT,
        is_banned=False,
):
    """ create user"""
    permission = UserPermissions.objects.get(group_name=user_group)
    profile = Profile.objects.create(school_name='THU', )
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


def createBank(
        name,
        root_id=1,
        picture="",
        brief="",
        createTime=timezone.now(),
        lastUpdate=timezone.now(),
        authority="public",
        question_count=0,
        invitation_code_count=0,
        activated_code_count=0,
):
    bank = QuestionBank.objects.create(
        root_id=root_id,
        name=name,
        picture=picture,
        brief=brief,
        createTime=createTime,
        lastUpdate=lastUpdate,
        authority=authority,
        question_count=question_count,
        invitation_code_count=invitation_code_count,
        activated_code_count=activated_code_count,
    )
    return bank


createBank("test_bank")
