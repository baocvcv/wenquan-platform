"""This code defines the model of choice questions"""
from django.db import models
from django.contrib.postgres.fields import ArrayField
from .question import Question


class FillBlankQ(Question):
    """Inherit from Question, model of choice question
    Attributes:
        question_content: the main content of the question
        question_blank_num: the num of blanks
        question_image: the image of the question
        qusetion_ans: the correct answer of the question
        question_solution: the specific solution of the question
    """
    question_content = ArrayField(ArrayField(models.CharField()))
    question_blank_num = models.IntegerField()
    question_image = ArrayField(ArrayField(models.CharField()))
    question_ans = ArrayField(models.CharField())
    question_solution = models.CharField()
