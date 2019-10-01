"""This code defines the model of brief answer questions"""
from django.db import models
from django.contrib.postgres.fields import ArrayField
from .question import Question


class BriefAnswerQ(Question):
    """Inherit from Question, model of brief answer question
    Attributes:
        question_content: the main content of the question
        question_image: the image of the question
        qusetion_ans: the correct answer of the question
        question_solution: the specific solution of the question
    """
    question_content = models.CharField()
    question_image = ArrayField(ArrayField(models.CharField()))
    question_ans = models.CharField()
    question_solution = models.CharField()
