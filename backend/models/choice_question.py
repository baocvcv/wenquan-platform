"""This code defines the model of choice questions"""
from django.db import models
from django.contrib.postgres.fields import ArrayField
from .question import Question


class ChoiceQ(Question):
    """Inherit from Question, model of choice question
    Attributes:
        question_content: the main content of the question
        question_image: the image of the question
        question_choice: the choices of the question, only one of them is correct
        question_solution: the specific solution of the question
    """
    question_content = models.CharField()
    question_image = ArrayField(ArrayField(models.CharField()))
    question_choice = ArrayField(models.CharField)
    question_solution = models.CharField()


class SingleChoiceQ(ChoiceQ):
    """Model of single choice question
    Attributes:
        qusetion_ans: the correct answer of the question
    """
    question_ans = models.CharField()


class MultpChoiceQ(ChoiceQ):
    """Model of multiple choices question
    Attributes:
        qusetion_ans: the correct answer of the question
        qusetion_ans_num: the num of correct answer
    """
    question_ans = ArrayField(models.CharField())
    question_ans_num = models.IntegerField()
