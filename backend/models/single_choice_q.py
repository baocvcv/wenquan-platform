"""This code defines the model of single choice question"""
from django.db import models
from django.contrib.postgres.fields import ArrayField
from .question import Question


class SingleChoiceQ(Question):
    """Inherit from Question
    Attributes:
        question_content: the main content of the question
        question_image: the image of the question
        question_choice: the choices of the question, only one of them is correct
        qusetion_ans: the correct answer of the question
        question_solution: the specific solution of the question
    """
    question_content = models.CharField()
    question_image = ArrayField(ArrayField(models.CharField()))
    question_choice = ArrayField(models.CharField)
    question_ans = models.CharField()
    question_solution = models.CharField()
    question_tags = ArrayField(models.CharField())
