"""Model for relationship between Question and Section"""
from django.db import models
from django.contrib.postgres.fields import ArrayField
from polymorphic.models import PolymorphicModel

from .paper import Section
from .questions.question import Question


class QuestionVersion(PolymorphicModel):
    '''Intermediary models for Paper and Question
    Attributes:
        paper: through_fields
        question: through_field
        question_version: the change_time of question saved in this paper
    '''

    section = models.ForeignKey(Section, on_delete=models.CASCADE, default=None)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_point = models.IntegerField(default=0)
    point_every_blank = ArrayField(models.IntegerField(), default=list)
    question_num = models.IntegerField()
