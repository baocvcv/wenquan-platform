"""test module for question_views"""
from copy import copy

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.models.questions import Question

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
            "question_level": 5,
            "question_content": "人类的本质是复读机吗?",
            "question_image": [""],
            "question_ans": True,
            "question_solution": "因为人类的本质是复读机"
        },
    ]

    fill_blank_example = [
        {
            "parents_node": [],
            "question_name": "question4",
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
        """Create test bank and node"""
        root = KnowledgeNode.objects.create(name="unnamed node")
        cls.bank_data['root_id'] = root.id
        serializer = QuestionBankSerializer(data=cls.bank_data)
        if serializer.is_valid():
            cls.bank = serializer.save()
            root.question_bank = cls.bank
            root.save()
        else:
            print(serializer.errors)

    def get_response(self, new_q_id):
        """GET method testing"""
        url = reverse("questions_detail", args=[new_q_id])
        response = self.client.get(url)
        return response

    def create_question(self, data):
        """Create Question from data by POST method"""
        url = reverse('questions_list')
        data[0]["parents_node"] = [self.bank.root_id]
        response = self.client.post(url, data, format='json')
        return response

    def test_single(self):
        """ test creating an single choice question"""
        data = copy(self.single_example)
        response = self.create_question(data)

        new_q = Question.objects.all()[0]
        new_q.checker(data['question_ans'])
        new_q.checker("")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_q.question_name, 'question1')
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(new_q.question_choice, ["A.复读机", "B.鸽子", "C.真香", "D.以上选项均正确"])

        response2 = self.get_response(new_q.id)
        self.assertEqual(response.data, response2.data)

    def test_multiple(self):
        """ test creating an single choice question"""
        data = copy(self.multi_example)
        response = self.create_question(data)

        new_q = Question.objects.all()[0]
        new_q.checker(data['question_ans'])
        new_q.checker([""])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_q.question_name, 'question2')
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(new_q.question_choice, ["A.复读机", "B.鸽子", "C.真香", "D.草履虫"])

        response2 = self.get_response(new_q.id)
        self.assertEqual(response.data, response2.data)

    def test_true_or_false(self):
        """ test creating an single choice question"""
        data = copy(self.t_or_f_example)
        response = self.create_question(data)

        new_q = Question.objects.all()[0]
        new_q.checker(data['question_ans'])
        new_q.checker(not data['question_ans'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_q.question_name, 'question3')
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(new_q.question_ans, True)

        response2 = self.get_response(new_q.id)
        self.assertEqual(response.data, response2.data)

    def test_fill_blank(self):
        """ test creating an single choice question"""
        data = copy(self.fill_blank_example)
        response = self.create_question(data)

        new_q = Question.objects.all()[0]
        new_q.checker(data['question_ans'])
        new_q.checker(["a"])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_q.question_name, 'question4')
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(new_q.question_content, ["人类的本质是", "和", "还有", ""])

        response2 = self.get_response(new_q.id)
        self.assertEqual(response.data, response2.data)

    def test_brief_ans(self):
        """ test creating an single choice question"""
        data = copy(self.brief_q_example)
        response = self.create_question(data)

        new_q = Question.objects.all()[0]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_q.question_name, 'question5')
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(new_q.question_ans, "复读机")

        response2 = self.get_response(new_q.id)
        self.assertEqual(response.data, response2.data)
