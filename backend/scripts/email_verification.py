""" Utils for email verification """
from random import Random
from django.core.mail import send_mail 
from django.utils import timezone

from backend.models import EmailVerificationRecord
from backend.models import User

def generate_token(len=30):
    ''' generate verification code '''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    random.seed(timezone.now())
    token = [chars[random.randint(0, length)] for i in range(len)]
    return token

def create_email_verification_record(user: User, send_type="register"):
    ''' generate verification record '''
    token = random_str()
    record = EmailVerificationRecord(
        user=user,
        token=token,
        email=user.email,
        send_type=send_type
    )
    record.save()
    record.send_email()
