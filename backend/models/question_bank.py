"""Define the model of Question Banks"""
from django.db import models
from polymorphic.models import PolymorphicModel

MAX_ID = 20
MAX_NAME = 200


class QuestionBanks(PolymorphicModel):
    """Models for Question Banks
    Attributes:
        name: name of bank
        subnodes: children Knowledg Node of bank
        questions: children question of bank
    """
    root_id = models.IntegerField()
    name = models.CharField(max_length=MAX_NAME)
