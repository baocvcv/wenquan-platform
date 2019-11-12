""" Authorization code """
from django.db import models
from django.utils import timezone

from backend.models import QuestionBank

class AuthCode(models.Model):
    """ Auth code model """
    key = models.CharField(max_length=30)
    time_generated = models.DateTimeField(auto_now=True)
    is_usable = models.BooleanField(default=True)
    question_bank = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
