"""test module for question_views"""
from copy import copy

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.models.questions import Question

from backend.models.knowledge_node import KnowledgeNode
from backend.serializers.question_bank_serializer import QuestionBankSerializer

from backend.models import UserPermissions
from backend.models import User
from backend.models import Profile
from backend.tests.utils import create_permission


def create_user(
        username,
        password="11111111",
        email="a@b.com",
        user_group=User.STUDENT,
        is_banned=False,
):
    """ create user"""
    permission = UserPermissions.objects.get(group_name=user_group)
    profile = Profile.objects.create(school_name='THU', )
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        user_group=user_group,
        user_permissions=permission,
        profile=profile,
        is_banned=is_banned,
        question_banks=[],
    )
    if user_group == 'Admin':
        user.is_staff = True
    if user_group == 'SuperAdmin':
        user.is_superuser = True
    return user


class QuestionTest(APITestCase):
    """ test for question views """
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

        create_permission().save()
        create_permission("Admin").save()
        create_permission("SuperAdmin").save()
        admin = create_user(username='xq', user_group=User.SUPER_ADMIN)
        admin.save()
        cls.user = admin

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
        new_q.checker(data[0]['question_ans'])
        new_q.checker("")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_q.question_name, 'question1')
        self.assertEqual(new_q.question_choice, ["A.复读机", "B.鸽子", "C.真香", "D.以上选项均正确"])

        response2 = self.get_response(new_q.id)
        self.assertEqual(response.data, response2.data)

        url = reverse("questions_detail", args=[new_q.id])
        data[0]["parents_node"] = [self.bank.root_id]
        data[0]["question_name"] = "modify"
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.data['question_name'], "modify")

    def test_multiple(self):
        """ test creating an single choice question"""
        data = copy(self.multi_example)
        response = self.create_question(data)

        new_q = Question.objects.all()[0]
        new_q.checker(data[0]['question_ans'])
        new_q.checker([""])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_q.question_name, 'question2')
        self.assertEqual(new_q.question_choice, ["A.复读机", "B.鸽子", "C.真香", "D.草履虫"])

        response2 = self.get_response(new_q.id)
        self.assertEqual(response.data, response2.data)

    def test_true_or_false(self):
        """ test creating an single choice question"""
        data = copy(self.t_or_f_example)
        response = self.create_question(data)

        new_q = Question.objects.all()[0]
        new_q.checker(data[0]['question_ans'])
        new_q.checker(not data[0]['question_ans'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_q.question_name, 'question3')
        self.assertEqual(new_q.question_ans, True)

        response2 = self.get_response(new_q.id)
        self.assertEqual(response.data, response2.data)

    def test_fill_blank(self):
        """ test creating an single choice question"""
        data = copy(self.fill_blank_example)
        response = self.create_question(data)

        new_q = Question.objects.all()[0]
        new_q.checker(data[0]['question_ans'])
        new_q.checker(["a"])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_q.question_name, 'question4')
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
        self.assertEqual(new_q.question_ans, "复读机")

        response2 = self.get_response(new_q.id)
        self.assertEqual(response.data, response2.data)

    def test_question_bank(self):
        """Test related to QuestionBank"""
        self.client.force_authenticate(user=self.user)  # pylint:disable=no-member

        url = reverse("banks_detail", args=[self.bank.id])
        self.client.get(url)

        url = reverse("banks_list")
        bank_post = {
            "name": "bank1",
            "picture": "www.a.com",
            "brief": "nothing here",
            "authority": "public",
            "invitation_code_count": 100,
        }
        response = self.client.post(url, bank_post, format='json')
        self.assertEqual(response.data["name"], "bank1")

    def test_nodes(self):
        """Test related to KnowledgeNode"""
        self.client.force_authenticate(user=self.user)  # pylint:disable=no-member

        self.create_question(self.multi_example)
        self.create_question(self.fill_blank_example)
        self.create_question(self.t_or_f_example)

        url = reverse("questions_list")
        self.client.get(url)

        url = reverse("nodes_list", args=[self.bank.root_id])
        self.client.get(url)
        node_data = {
            "delete": [],
            "modify": {
                "id": self.bank.root_id,
                "name": "math",
                "subnodes": [
                    {
                        "id": -1,
                        "name": "algebra",
                        "subnodes": [
                            {
                                "id": -1,
                                "name": "circle",
                                "subnodes": [],
                            },
                        ]
                    },
                ]
            }
        }
        response = self.client.put(url, node_data, format='json')
        node_id = response.data["subnodes"][0]['id']
        node_data['delete'] = [node_id]
        self.client.put(url, node_data, format='json')

        url = reverse("nodes_detail", args=[self.bank.root_id])
        self.client.get(url)

        url = reverse("nodes_question")
        self.client.post(url, {"nodes_id": [self.bank.root_id]}, format='json')

    def test_paper(self):
        "Test related to Paper"

        self.client.force_authenticate(user=self.user)  # pylint:disable=no-member
        sing = self.create_question(self.single_example).data
        mult = self.create_question(self.multi_example).data
        fill = self.create_question(self.fill_blank_example).data
        torf = self.create_question(self.t_or_f_example).data

        paper_data = {
            "title":
            "test paper",
            "total_point":
            100,
            "tips":
            "",
            "status":
            "public",
            "sections": [{
                "title": "select",
                "total_point": 50,
                "section_num": 1,
                "questions": [{
                    "id": sing['id'],
                    "question_point": 10,
                    "point_every_blank": [],
                    "question_num": 1
                }, {
                    "id": mult['id'],
                    "question_point": 15,
                    "point_every_blank": [],
                    "question_num": 2
                }, {
                    "id": fill['id'],
                    "question_point": 25,
                    "point_every_blank": [1],
                    "question_num": 3
                }]
            }, {
                "title": "unnamed sections",
                "total_point": 50,
                "section_num": 2,
                "questions": [
                    {
                        "id": torf['id'],
                        "question_point": 25,
                        "point_every_blank": [],
                        "question_num": 1
                    },
                ]
            }]
        }
        url = reverse("papers_list")
        response = self.client.post(url, paper_data, format='json')
        self.client.get(url)
        self.assertEqual(response.data['title'], paper_data['title'])

        instance = Question.objects.get(id=sing['id'])
        instance.checker(sing['question_ans'], 1)

        instance = Question.objects.get(id=mult['id'])
        instance.checker(mult['question_ans'], 1)

        instance = Question.objects.get(id=fill['id'])
        instance.checker(fill['question_ans'], 1)

        instance = Question.objects.get(id=torf['id'])
        instance.checker(torf['question_ans'], 2)

        paper_id = response.data['id']
        url = reverse("papers_detail", args=[paper_id])
        self.client.get(url)

        paper_data['status'] = "drafted"
        self.client.put(url, paper_data, format='json')

        change_state = {"change_status": "error"}
        self.client.put(url, change_state, format='json')

        change_state = {"change_status": "drafted"}
        self.client.put(url, change_state, format='json')
