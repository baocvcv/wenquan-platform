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
from backend.models.knowledge_node import KnowledgeNode
from backend.models.questions.question import TYPEDIC


class QuestionList(APIView):
    """Get all questions info or create a question"""
    def get(self, request):
        """get all questions, only get the latest version"""
        question_groups = QuestionGroup.objects.get()
        response = []
        for i in question_groups:
            question = i.history_version_set().get(question_change_time=i.current_version)
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

            nodes = []
            for j in i.parents_node.all():
                nodes += j.id
            if serializer.is_valid():
                question_info = serializers.data
                question_info['id'] = question.id
                question_info.pop('history_version')
                question_info['parents_node'] = nodes
                response += question_info
        return Response(response)

    def post(self, request):
        """Create a question"""
        post_data = JSONParser().parse(request)[0]
        post_data.pop('id')
        parents_id = post_data.pop('parents_node')
        post_data['question_change_time'] = timezone.now()
        parents = []
        for i in parents_id:
            node = KnowledgeNode.objects.get(id=i)
            parents += node
        bank = node.question_bank
        q_group = QuestionGroupSerializer(
            current_version=post_data['question_change_time'],
            belong_bank=bank,
            parents_node=parents,
        )

        post_data['history_version'] = q_group
        post_data['question_type'] = TYPEDIC[post_data['question_type']]

        if post_data['question_type'] == TYPEDIC['single']:
            question = SingleChoiceQSerializer(**post_data)
        elif post_data['question_type'] == TYPEDIC['multiple']:
            question = MultpChoiceQSerializer(**post_data)
        elif post_data['question_type'] == TYPEDIC['TorF']:
            question = TrueOrFalseQSerializer(**post_data)
        elif post_data['question_type'] == TYPEDIC['fill_blank']:
            question = FillBlankQSerializer(**post_data)
        elif post_data['question_type'] == TYPEDIC['brief_ans']:
            question = BriefAnswerQSerializer(**post_data)

        if q_group.is_valid() and question.is_valid:
            new_q = question.save()
            response = question.data
            response['id'] = new_q.id
            response['parents_node'] = post_data['parents_node']
            return Response(response, status=201)
        return Response(question.errors, status=400)
