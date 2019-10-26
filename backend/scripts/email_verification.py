""" Utils for email verification """
from random import Random
from django.core.mail import send_mail
from django.utils import timezone
from rest_framework import status

from backend.models import EmailVerificationRecord
from backend.models import User
from backend.serializers import UserSerializer

def generate_token(token_len=30):
    ''' generate verification code '''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    random.seed(timezone.now())
    token = ''
    for _ in range(token_len):
        token += chars[random.randint(0, length)]
    return token

def create_email_verification_record(user: User, send_type="register"):
    ''' generate verification record '''
    token = generate_token()
    print(token)
    record = EmailVerificationRecord(
        user=user,
        token=token,
        email=user.email,
        send_type=send_type,
    )
    record.save()
    record.send_email()

def use_token(token, password=None):
    """ check if token exists and is valid """
    record = EmailVerificationRecord.objects.get(token=token)
    if record is None or not record.is_valid:
        msg = {"token": "Token does not exist"}
        sta = status.HTTP_400_BAD_REQUEST
        return msg, sta
    user = record.user
    if record.is_time_valid(timezone.now()):
        record.is_valid = False
        record.save()
        if record.send_type == "forget":
            if password is None:
                msg = {"error": "No password received"}
                sta = status.HTTP_400_BAD_REQUEST
                return msg, sta
            user.set_password(password)
            user.save()
        elif record.send_type == "register":
            user.is_active = True
            user.save()
        msg = UserSerializer(user).data
        sta = status.HTTP_200_OK
        return msg, sta
    msg = {"error": "Token has expired!"}
    sta = status.HTTP_400_BAD_REQUEST
    return msg, sta
