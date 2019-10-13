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
    questions = models.ManyToManyField(
        QuestionGroup,
        through='QuestionVersion',
        through_fields=('paper', 'question'),
    )


class QuestionVersion(PolymorphicModel):
    '''Intermediary models for Paper and Question
    Attributes:
        paper: through_fields
        question: through_field
        question_version: the change_time of question saved in this paper
    '''
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionGroup, on_delete=models.CASCADE)
    question_version = models.DateTimeField()
