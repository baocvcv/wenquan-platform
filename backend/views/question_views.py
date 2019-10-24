""" Questino view """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.utils import timezone

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
    @staticmethod
    def question_to_serializer(question):
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

    def get(self, request):
        """get all questions, only get the latest version"""

        question_groups = QuestionGroup.objects.all()
        response = []

        for i in question_groups:
            if len(i.question_set.all()) == 0:
                continue
            question = i.question_set.all().get(question_change_time=i.current_version)

            serializer = self.question_to_serializer(question)

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

        if question.is_valid():
            new_q = question.save()
            response = question.data
            response['id'] = new_q.id
            bank.question_count = len(bank.questiongroup_set.all())
            response['question_type'] = INT2TYPE[(str)(response['question_type'])]
            return Response(response, status=201)
        return Response(question.errors, status=400)


class QuestionDetail(APIView):
    def get(self, request, pk):
        question = Question.objects.get(id=pk)
        serializer = QuestionList.question_to_serializer(question)
        response = serializer.data
        response['question_type'] = INT2TYPE[(str)(response['question_type'])]
        return Response(response)

    def put(self, request, pk):
        put_data = JSONParser().parse(request)[0]
        put_data.pop('id')
        question = Question.objects.get(id=pk)
        qtype = question.question_type
        if qtype == TYPEDIC['single']:
            serializer = SingleChoiceQSerializer(question, put_data)
        elif qtype == TYPEDIC['multiple']:
            serializer = MultpChoiceQSerializer(question, put_data)
        elif qtype == TYPEDIC['TorF']:
            serializer = TrueOrFalseQSerializer(question, put_data)
        elif qtype == TYPEDIC['fill_blank']:
            serializer = FillBlankQSerializer(question, put_data)
        elif qtype == TYPEDIC['brief_ans']:
            serializer = BriefAnswerQSerializer(question, put_data)

        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            response['question_type'] = INT2TYPE[(str)(response['question_type'])]
            return Response(response, status=200)
        return Response(serializer.erorrs, status=400)
