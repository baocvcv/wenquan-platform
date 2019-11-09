"""This code defines the model of ture of false questions"""
from django.db import models
from django.contrib.postgres.fields import ArrayField

from backend.models.paper import Section
from .question import Question, MAX_URL, MAX_CONTENT


class TrueOrFalseQ(Question):
    """Inherit from Question, model of true and false question
    Attributes:
        question_content: the main content of the question
        question_image: the image of the question
        qusetion_ans: the correct answer of the question
        question_solution: the specific solution of the question
    """
    question_content = models.CharField(max_length=MAX_CONTENT)
    question_image = ArrayField(models.CharField(max_length=MAX_URL))
    question_ans = models.BooleanField()
    question_solution = models.CharField(max_length=MAX_CONTENT)

    def checker(self, ans, section_id=None):
        """Checker for TrueOrFalseQ"""
        point = -1
        if section_id is not None:
            point = 0
            section = Section.objects.get(id=section_id)
            if not section:
                return "Not Found"
            q_on_paper = section.questionversion_set.get(question=self, section=section)
        if ans == self.question_ans:
            if section_id is not None:
                point = q_on_paper.question_point
            return True, [point]
        return False, [point]
