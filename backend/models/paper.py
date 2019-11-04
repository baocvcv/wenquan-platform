'''Code for models: paper'''
from django.db import models
from django.contrib.postgres.fields import ArrayField
from polymorphic.models import PolymorphicModel
from .questions.question import Question

MAX_NAME = 200


class Paper(PolymorphicModel):
    '''Model of Paper
    Attributes:
        name: the name of a paper
        title: title of the paper
        total_points: total points of test paper
        tips: tips provided for students
        sections: a list of sections []
        status: published or drafted
    '''
    name = models.CharField(max_length=MAX_NAME, default="unmaned paper")
    title = models.CharField(max_length=MAX_NAME, default="unmaned paper")
    total_point = models.IntegerField(default=100)
    tips = ArrayField(models.CharField(max_length=MAX_NAME), default=list)
    status = models.CharField(max_length=MAX_NAME, default="drafted")
    is_latest = models.BooleanField(default=True)


class Section(PolymorphicModel):
    '''Model of Sections in paper
    Attributes:
        name: name of the section title: title of the section
        total_points: total_points of the section
        questions:a list of questions
    '''
    name = models.CharField(max_length=MAX_NAME)
    title = models.CharField(max_length=MAX_NAME)
    total_point = models.IntegerField()
    belong_paper = models.ForeignKey(Paper, on_delete=models.CASCADE, null=True)
    section_num = models.IntegerField()
    questions = models.ManyToManyField(
        Question,
        through='QuestionVersion',
        through_fields=('section', 'question'),
    )


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
    question_num = models.IntegerField()
