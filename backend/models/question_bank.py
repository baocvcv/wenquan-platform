"""Define the model of Question Banks"""
from django.db import models
from polymorphic.models import PolymorphicModel

MAX_CONTENT = 20000
MAX_ID = 20
MAX_NAME = 200
MAX_URL = 10000000


class QuestionBank(PolymorphicModel):
    """Models for Question Banks
    Attributes:
        name: name of bank
        subnodes: children Knowledge Node of bank
        questions: children question of bank
    """
    root_id = models.IntegerField()
    name = models.CharField(max_length=MAX_NAME)
    picture = models.CharField(max_length=MAX_URL)
    brief = models.CharField(max_length=MAX_CONTENT)
    createTime = models.DateTimeField()
    lastUpdate = models.DateTimeField()
    authority = models.CharField(max_length=MAX_NAME)
    question_count = models.IntegerField()
    invitation_code_count = models.IntegerField()
    activated_code_count = models.IntegerField()
