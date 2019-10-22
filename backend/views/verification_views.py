""" Views for verification """
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from backend.models import User
from backend.models import EmailVerificationRecord

from backend.scripts.email_verification import create_email_verification_record
