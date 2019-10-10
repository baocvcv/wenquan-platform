from backend.models import questions
from django.test import TestCase
import datetime


class QuestionTest(TestCase):
    def setUp(self):
        questions.question.Question.objects.create(
            question_id=0,
            question_name='base',
            question_change_time=datetime.data(),
        )

    def test_base_question(self):
        models.questions.question.Question
        pass
