""" Questino view """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.utils import timezone
from django.http import Http404

from backend.serializers.question_serializer import SingleChoiceQSerializer
from backend.serializers.question_serializer import MultpChoiceQSerializer
from backend.serializers.question_serializer import TrueOrFalseQSerializer
from backend.serializers.question_serializer import FillBlankQSerializer

from backend.serializers.question_serializer import BriefAnswerQSerializer

from backend.models.questions import QuestionGroup
from backend.models.questions import Question
from backend.models.knowledge_node import KnowledgeNode
from backend.models.questions.question import TYPEDIC
from backend.models.questions.question import INT2TYPE


class QuestionList(APIView):
    """Get all questions info or create a question"""
    @classmethod
    def create_question_from_data(cls, post_data):
        """Create diffrent types of Question objects from json"""
        post_data['question_type'] = TYPEDIC[post_data['question_type']]
        if post_data['question_type'] == TYPEDIC['single']:
            question = SingleChoiceQSerializer(data=post_data)
        elif post_data['question_type'] == TYPEDIC['multiple']:
            question = MultpChoiceQSerializer(data=post_data)
        elif post_data['question_type'] == TYPEDIC['TorF']:
            question = TrueOrFalseQSerializer(data=post_data)
        elif post_data['question_type'] == TYPEDIC['fill_blank']:
            question = FillBlankQSerializer(data=post_data)
        elif post_data['question_type'] == TYPEDIC['brief_ans']:
            question = BriefAnswerQSerializer(data=post_data)
        return question

    @classmethod
    def create_serializer_from_question(cls, question):
        """Create diffrent Serializer from Question"""
        qtype = question.question_type
        if qtype == TYPEDIC['single']:
            serializer = SingleChoiceQSerializer(question)
        elif qtype == TYPEDIC['multiple']:
            serializer = MultpChoiceQSerializer(question)
        elif qtype == TYPEDIC['TorF']:
            serializer = TrueOrFalseQSerializer(question)
        elif qtype == TYPEDIC['fill_blank']:
            serializer = FillBlankQSerializer(question)
        elif qtype == TYPEDIC['brief_ans']:
            serializer = BriefAnswerQSerializer(question)
        return serializer

    @classmethod
    def get_latest_version(cls, q_group):
        """Get the latest version of a Question"""
        try:
            return q_group.question_set.all().get(question_change_time=q_group.current_version)
        except q_group.question_set.all().DoesNotExist:
            raise Http404

    def get(self, request):
        """get all questions, only get the latest version"""
        question_groups = QuestionGroup.objects.all()
        response = []

        for i in question_groups:
            if not i.question_set.all():
                continue

            question = self.get_latest_version(i)
            serializer = self.create_serializer_from_question(question)

            nodes = []
            for j in i.parents_node.all():
                nodes.append(j.id)
            question_info = serializer.data
            question_info['id'] = question.id
            question_info['parents_node'] = nodes
            question_info['question_type'] = INT2TYPE[(str)(question_info['question_type'])]
            response.append(question_info)

        return Response(response)

    def post(self, request):
        """Create a question"""

        post_data = JSONParser().parse(request)[0]
        post_data.pop('id')
        parents_id = post_data.pop('parents_node')

        parents = []
        for i in parents_id:
            node = KnowledgeNode.objects.get(id=i)
            parents.append(node)

        bank = node.question_bank

        q_group = QuestionGroup(
            current_version=timezone.now(),
            belong_bank=bank,
        )

        q_group.save()
        q_group.parents_node.set(parents)
        q_group.save()

        post_data['question_change_time'] = q_group.current_version
        post_data['history_version_id'] = q_group.id

        question = self.create_question_from_data(post_data)

        if question.is_valid():
            new_q = question.save()
            response = question.data
            response['id'] = new_q.id
            bank.question_count = len(bank.questiongroup_set.all())
            bank.lastUpdate = q_group.current_version
            bank.save()
            response['question_type'] = INT2TYPE[(str)(response['question_type'])]
            response['parents_node'] = parents_id
            return Response(response, status=201)
        return Response(question.errors, status=400)


class QuestionDetail(APIView):
    """View for one Question"""
    @classmethod
    def get_object(cls, q_id):
        """Get Question with id=q_id"""
        try:
            return Question.objects.get(id=q_id)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, q_id):
        """Get information of the Question whose id=q_id"""
        question = self.get_object(q_id)
        serializer = QuestionList.create_serializer_from_question(question)
        response = serializer.data
        response['question_type'] = INT2TYPE[(str)(response['question_type'])]
        q_group = question.history_version
        nodes = []
        for i in q_group.parents_node.all():
            nodes.append(i.id)
        response['parents_node'] = nodes
        return Response(response)

    def put(self, request, q_id):
        """Upate information of the Question whose id=q_id"""
        post_data = JSONParser().parse(request)[0]
        old_q = self.get_object(q_id)

        q_group = old_q.history_version
        q_group.current_version = timezone.now()
        q_group.save()

        post_data['question_change_time'] = q_group.current_version
        post_data['history_version_id'] = q_group.id

        question = QuestionList.create_question_from_data(post_data)

        if question.is_valid():
            new_q = question.save()
            response = question.data
            response['id'] = new_q.id
            response['question_type'] = INT2TYPE[(str)(response['question_type'])]
            new_parents = []
            for i in post_data['parents_node']:
                new_parents.append(KnowledgeNode.objects.get(id=i))
            q_group.parents_node.set(new_parents)

            response['parents_node'] = post_data['parents_node']
            return Response(response, status=201)
        return Response(question.errors, status=400)
