"""This code defines the model of choice questions"""
from django.db import models
from django.contrib.postgres.fields import ArrayField
from .question import Question, MAX_URL, MAX_CONTENT


class ChoiceQ(Question):
    """Inherit from Question, model of choice question
    Attributes:
        question_content: the main content of the question
        question_image: the image of the question
        question_choice: the choices of the question, only one of them is correct
        question_solution: the specific solution of the question
    """
    question_content = models.CharField(max_length=MAX_CONTENT)
    question_image = ArrayField(ArrayField(models.URLField(max_length=MAX_URL)))
    question_choice = ArrayField(models.CharField(max_length=MAX_CONTENT))
    question_solution = models.CharField(max_length=MAX_CONTENT)


class SingleChoiceQ(ChoiceQ):
    """Model of single choice question
    Attributes:
        qusetion_ans: the correct answer of the question
    """
    question_ans = models.CharField(max_length=10)


class MultpChoiceQ(ChoiceQ):
    """Model of multiple choices question
    Attributes:
        qusetion_ans: the correct answer of the question
        qusetion_ans_num: the num of correct answer
    """
    question_ans = ArrayField(models.CharField(max_length=10))
    question_ans_num = models.IntegerField()
