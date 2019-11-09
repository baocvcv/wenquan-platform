"""This code defines the model of choice questions"""
from django.db import models
from django.contrib.postgres.fields import ArrayField
from .question import Question, MAX_URL, MAX_CONTENT
from backend.views.paper_views import SectionDetail


class ChoiceQ(Question):
    """Inherit from Question, model of choice question
    Attributes:
        question_content: the main content of the question
        question_image: the image of the question
        question_choice: the choices of the question, only one of them is correct
        question_solution: the specific solution of the question
    """
    question_content = models.CharField(max_length=MAX_CONTENT)
    question_image = ArrayField(models.CharField(max_length=MAX_URL))
    question_choice = ArrayField(models.CharField(max_length=MAX_CONTENT))
    question_solution = models.CharField(max_length=MAX_CONTENT)


class SingleChoiceQ(ChoiceQ):
    """Model of single choice question
    Attributes:
        qusetion_ans: the correct answer of the question
    """
    question_ans = models.CharField(max_length=10)

    def checker(self, ans, section_id=None):
        """Checker for SingleChoiceQ"""
        point = -1
        if section_id is not None:
            section = SectionDetail.get_object(section_id)
            q_on_paper = section.questionversion_set.get(question=self, section=section)
            point = 0
        if self.question_ans == ans:
            if section_id is not None:
                point = q_on_paper.question_point
            return True, [point]
        return False, [point]


class MultpChoiceQ(ChoiceQ):
    """Model of multiple choices question
    Attributes:
        qusetion_ans: the correct answer of the question
        qusetion_ans_num: the num of correct answer
    """
    question_ans = ArrayField(models.CharField(max_length=10))
    question_ans_num = models.IntegerField()

    def checker(self, ans, setion_id=None):
        """Checker for MultpChoiceQ"""
        point = -1
        correct = 0
        correct_ans = set(self.question_ans)
        ans = set(ans)
        if paper_id is not None:
            section = SectionDetail.get_object(section_id)
            q_on_paper = section.questionversion_set.get(question=self, section=section)
            point = 0
        if ans.issubset(correct_ans):
            correct = 0.5
            if correct_ans.issubset(ans):
                correct = 1
            if paper_id is not None:
                point = q_on_paper.question_point * correct
        if correct == 1:
            return True, [point]
        return False, [point]
