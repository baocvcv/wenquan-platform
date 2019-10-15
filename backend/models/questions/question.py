"""This code define the BASE model of question """
from enum import IntEnum
from django.db import models
from polymorphic.models import PolymorphicModel
from .question_group import QuestionGroup

MAX_ID = 20
MAX_URL = 200
MAX_NAME = 200
MAX_CONTENT = 20000


class Question(PolymorphicModel):
    """Base class of the question
    only identity infomation, NOT specific infomation of question

    Attributes:
        history_version: QuestionGroup record a question's change history
        question_id: each question has a unique id
        question_name: names of the questions
        qustion_type: there are 5 type, more info in enum Type
        question_level: the level of difficulty
        question_change_time: the time of last change
    """
    Type = IntEnum(
        'Type',
        (
            'single_choice',  # single choice question
            'multiple_choice',  # multiple choices question
            't_or_f',  # true or false question
            'fill_blank',  # fill the blank question
            'q_and_a',  # short answer question
        ))
    history_version = models.ForeignKey(QuestionGroup, on_delete=models.CASCADE)
    question_id = models.CharField(max_length=MAX_ID)
    question_name = models.CharField(max_length=MAX_NAME)
    question_type = models.IntegerField()
    question_level = models.FloatField(default=0)
    question_change_time = models.DateTimeField()
