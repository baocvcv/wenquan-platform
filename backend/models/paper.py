'''Code for models: paper'''
from django.db import models
from polymorphic.models import PolymorphicModel
from .questions import QuestionGroup

MAX_NAME = 200


class Paper(PolymorphicModel):
    '''Model of Paper
    Attributes:
        name: the name of a paper
        questions: the questions of the paper
    '''
    name = models.CharField(max_length=MAX_NAME)
    questions = models.ManyToManyField(QuestionGroup)
