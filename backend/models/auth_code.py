""" Authorization code """
from django.db import models

from .question_bank import QuestionBank

class AuthCode(models.Model):
    """ Auth code model """
    key = models.CharField(max_length=30, unique=True)
    time_generated = models.DateTimeField(auto_now=True)
    is_usable = models.BooleanField(default=True)
    question_bank = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
