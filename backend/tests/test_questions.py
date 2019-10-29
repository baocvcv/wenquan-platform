"""test module for question_views"""
from copy import copy

# from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.models.questions import Question
from backend.models.questions import SingleChoiceQ
from backend.models.questions import MultpChoiceQ
from backend.models.questions import TrueOrFalseQ
from backend.models.questions import FillBlankQ
from backend.models.questions import BriefAnswerQ

from backend.models.question_bank import QuestionBank
from backend.models.knowledge_node import KnowledgeNode
from backend.serializers.question_bank_serializer import QuestionBankSerializer


class QuestionListViewTest(APITestCase):
    """ test for question views """
    bank = QuestionBank()
    bank_data = {
        "name": "bank1",
        "picture": "www.a.com",
        "brief": "nothing here",
        "authority": "public",
        "invitation_code_count": 100,
    }

    single_example = [
        {
            "parents_node": [],
            "question_name": "question1",
            "question_type": "single",
            "question_level": 5,
            "question_content": "人类的本质是?",
            "question_image": [""],
            "question_choice": ["A.复读机", "B.鸽子", "C.真香", "D.以上选项均正确"],
            "question_ans": "D",
            "question_solution": "某一时刻被观测时, 人类会坍缩为A,B,C中某一种情况"
        },
    ]

    multi_example = [
        {
            "parents_node": [],
            "question_name": "question2",
            "question_type": "multiple",
            "question_level": 5,
            "question_content": "人类的本质是?",
            "question_image": [""],
            "question_choice": ["A.复读机", "B.鸽子", "C.真香", "D.草履虫"],
            "question_ans": ["A", "B", "C"],
            "question_ans_num": 3,
            "question_solution": "某一时刻被观测时, 人类会坍缩为A,B,C中某一种情况"
        },
    ]

    t_or_f_example = [
        {
            "parents_node": [],
            "question_name": "question3",
            "question_type": "TorF",
            "question_level": 0.5,
            "question_content": "人类的本质是复读机吗?",
            "question_image": [""],
            "question_ans": True,
            "question_solution": "因为人类的本质是复读机"
        },
    ]

    fill_blank_example = [
        {
            "parents_node": [],
            "question_name": "quetsion4",
            "question_type": "fill_blank",
            "question_level": 5,
            "question_content": ["人类的本质是", "和", "还有", ""],
            "question_blank_num": 3,
            "question_image": [""],
            "question_ans": ["复读机", "鸽子", "真香"],
            "question_solution": "因为人类的本质是复读机,鸽子,真香"
        },
    ]

    brief_q_example = [
        {
            "parents_node": [],
            "question_name": "question5",
            "question_type": "brief_ans",
            "question_level": 5,
            "question_content": "人类的本质是?",
            "question_image": [""],
            "question_ans": "复读机",
            "question_solution": "因为人类的本质是复读机"
        },
    ]

    @classmethod
    def setUpTestData(cls):
        root = KnowledgeNode.objects.create(name="unnamed node")
        cls.bank_data['root_id'] = root.id
        serializer = QuestionBankSerializer(data=cls.bank_data)
        if serializer.is_valid():
            cls.bank = serializer.save()
            root.question_bank = cls.bank
            root.save()
        else:
            print(serializer.errors)

    def test_create_Single(self):
        """ test creating an single choice question"""
        url = reverse('questions_list')
        data = copy(self.single_example)
        data[0]["parents_node"] = [self.bank.root_id]
        response = self.client.post(url, data, format='json')

        new_q = Question.objects.all()[0]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(new_q.question_name, 'question1')
        self.assertEqual(new_q.question_choice, ["A.复读机", "B.鸽子", "C.真香", "D.以上选项均正确"])
