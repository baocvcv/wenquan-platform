'''unit test for questions models'''
import datetime
from django.test import TestCase
from django.utils import timezone
from backend.models.questions.question import Question
from backend.models.questions.fill_blank_q import FillBlankQ
# from backend.models.questions.choice_question import ChoiceQ, SingleChoiceQ, MultpChoiceQ
# from backend.models.questions.true_or_false_q import TrueOrFalseQ
# from backend.models.questions.brief_answer_q import BriefAnswerQ

NOW = datetime.datetime.NOW(tz=timezone.utc)


class QuestionTest(TestCase):
    '''unit test of base question class'''
    def setUp(self):
        '''Create a base question example'''
        Question.objects.create(
            question_id=0,
            question_name='base',
            question_type=0,
            question_level=0,
            question_change_time=NOW,
        )

    def test_base_question(self):
        '''check the example in database'''
        target = Question.objects.get(question_id='0')
        self.assertEqual(target.question_name, 'base')
        self.assertEqual(target.question_type, 0)
        self.assertEqual(target.question_level, 0)
        self.assertEqual(target.question_change_time, NOW)


class FillBlankQTest(TestCase):
    '''unit test of fill blank question class'''
    def setUp(self):
        '''create a fill blank question example'''
        FillBlankQ.objects.create(
            question_id=1,
            question_name='fill_blank',
            question_type=Question.Type.single_choice,
            question_level=0,
            question_change_time=NOW,
            question_image=['www.image.com'],
            question_solution='solution',
            question_blank_num='0',
            question_content=['0'],
            question_ans=[0],
        )

    def test_base_question(self):
        '''check the example saved in database'''
        target = FillBlankQ.objects.get(question_id='1')
        self.assertEqual(target.question_name, 'fill_blank')
        self.assertEqual(target.question_type, Question.Type.single_choice)
        self.assertEqual(target.question_level, 0)
        self.assertEqual(target.question_change_time, NOW)
