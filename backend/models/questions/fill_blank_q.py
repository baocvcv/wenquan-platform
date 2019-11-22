"""This code defines the model of fill blank questions"""
from django.db import models
from django.contrib.postgres.fields import ArrayField

from backend.models.paper import Section
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

    def checker(self, ans, section_id=None):
        """Checker for FillBlankQ"""
        if not section_id:
            if ans == self.question_ans:
                return True, []
            return False, []

        point = []
        section = Section.objects.get(id=section_id)

        if not section:
            return "Not Found"

        q_on_paper = section.questionversion_set.get(question=self, section=section)

        for i in range(0, len(self.question_ans)):
            if i >= len(ans):
                break
            if ans[i] == self.question_ans[i] and i < len(q_on_paper.point_every_blank):
                point.append(q_on_paper.point_every_blank[i])
            elif i < len(q_on_paper.point_every_blank):
                point.append(0)

        if ans == self.question_ans:
            return True, point
        return False, point
