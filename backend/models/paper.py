'''Code for models: paper'''
from django.db import models
from polymorphic.models import PolymorphicModel

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
    title = models.CharField(max_length=MAX_NAME, default="unmaned paper")
    total_point = models.IntegerField(default=100)
    tips = models.CharField(max_length=MAX_NAME, default="")
    status = models.CharField(max_length=MAX_NAME, default="drafted")
    is_latest = models.BooleanField(default=True)
    time_limit = models.IntegerField(default=0)
    have_brief_ans = models.BooleanField(default=True)


class Section(PolymorphicModel):
    '''Model of Sections in paper
    Attributes:
        name: name of the section title: title of the section
        total_points: total_points of the section
        questions:a list of questions
    '''
    title = models.CharField(max_length=MAX_NAME)
    total_point = models.IntegerField()
    belong_paper = models.ForeignKey(Paper, on_delete=models.CASCADE, null=True)
    section_num = models.IntegerField()
    questions = models.ManyToManyField(
        'Question',
        through='QuestionVersion',
        through_fields=('section', 'question'),
    )
