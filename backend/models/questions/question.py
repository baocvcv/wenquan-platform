"""This code define the BASE model of question """
from django.db import models
from polymorphic.models import PolymorphicModel
from .question_group import QuestionGroup

MAX_ID = 20
MAX_URL = 10000000
MAX_NAME = 200
MAX_CONTENT = 20000

TYPEDIC = {
    'single': 1,
    'multiple': 2,
    'TorF': 3,
    'fill_blank': 4,
    'brief_ans': 5,
}

INT2TYPE = {
    '1': 'single',
    '2': 'multiple',
    '3': 'TorF',
    '4': 'fill_blank',
    '5': 'brief_ans',
}


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
    history_version = models.ForeignKey(QuestionGroup, on_delete=models.CASCADE)
    question_name = models.CharField(max_length=MAX_NAME)
    question_type = models.IntegerField()
    question_level = models.IntegerField(default=0)
    question_change_time = models.DateTimeField()

    def checker(self, ans):
        response = {}
        if ans == self.ans:
            response['result'] = True
        else:
            response['result'] = False
        return response
