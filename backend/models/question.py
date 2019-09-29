"""This code define the BASE model of question """
from enum import Enum
from django.db import models


class Question(models.Model):
    """Base class of the question
    only identity infomation, NOT specific infomation of question

    Attributes:
        question_id: each question has a unique id
        question_name: names of the questions
        qustion_type: there are 5 type, more info in enum Type
        question_level: the level of difficulty
        question_change_time: the time of last change
    """
    Type = Enum(
        'Type',
        (
            'single_choice',  # single choice question
            'multiple_choice',  # multiple choices question
            't_or_f',  # true or false question
            'fill_blank',  # fill the blank question
            'q_and_a',  # short answer question
        ))
    question_id = models.IntegerField()
    question_name = models.CharField()
    question_type = models.IntegerField()
    question_level = models.FloatField()
    question_change_time = models.DateTimeField()
