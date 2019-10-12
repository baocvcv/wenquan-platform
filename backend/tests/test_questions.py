from backend.models.questions.question import Question
from backend.models.questions.fill_blank_q import FillBlankQ
# from backend.models.questions.choice_question import ChoiceQ, SingleChoiceQ, MultpChoiceQ
# from backend.models.questions.true_or_false_q import TrueOrFalseQ
# from backend.models.questions.brief_answer_q import BriefAnswerQ
from django.test import TestCase
import datetime
from django.utils import timezone

now = datetime.datetime.now(tz=timezone.utc)


class QuestionTest(TestCase):
    def setUp(self):
        Question.objects.create(
            question_id=0,
            question_name='base',
            question_type=0,
            question_level=0,
            question_change_time=now,
        )

    def test_base_question(self):
        a = Question.objects.get(question_id='0')
        self.assertEqual(a.question_name, 'base')
        self.assertEqual(a.question_type, 0)
        self.assertEqual(a.question_level, 0)
        self.assertEqual(a.question_change_time, now)


class FillBlankQTest(TestCase):
    def setUp(self):
        FillBlankQ.objects.create(
            question_id=1,
            question_name='fill_blank',
            question_type=Question.Type.single_choice,
            question_level=0,
            question_change_time=now,
            question_image=['www.image.com'],
            question_solution='solution',
            question_blank_num='0',
            question_content=['0'],
            question_ans=[0],
        )

    def test_base_question(self):
        a = FillBlankQ.objects.get(question_id='1')
        self.assertEqual(a.question_name, 'fill_blank')
        self.assertEqual(a.question_type, Question.Type.single_choice)
        self.assertEqual(a.question_level, 0)
        self.assertEqual(a.question_change_time, now)
