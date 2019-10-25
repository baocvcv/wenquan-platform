"""This code defines the model of fill blank questions"""
from django.db import models
from django.contrib.postgres.fields import ArrayField
from .question import Question, MAX_URL, MAX_CONTENT


class FillBlankQ(Question):
    """Inherit from Question, model of fill blank question
    Attributes:
        question_content: the main content of the question
        question_blank_num: the num of blanks
        question_image: the image of the question
        qusetion_ans: the correct answer of the question
        question_solution: the specific solution of the question
    """
    question_content = ArrayField(models.CharField(max_length=MAX_CONTENT))
    question_blank_num = models.IntegerField()
    question_image = ArrayField(models.CharField(max_length=MAX_URL))
    question_ans = ArrayField(models.CharField(max_length=MAX_CONTENT))
    question_solution = models.CharField(max_length=MAX_CONTENT)
