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
from backend.serializers.question_group_serializer import QuestionGroupSerializer
from backend.serializers.knowledge_node_serializer import KnowlegdeNodeSerializer
from backend.serializers.question_bank_serializer import QuestionBankSerializer

from backend.models.questions import QuestionGroup
from backend.models.questions import Question
from backend.models.knowledge_node import KnowledgeNode
from backend.models.questions.question import TYPEDIC


class QuestionList(APIView):
    """Get all questions info or create a question"""
    def get(self, request):
        """get all questions, only get the latest version"""
        question_groups = QuestionGroup.objects.all()
        response = []
        for i in question_groups:
            if len(i.question_set.all()) == 0:
                continue
            question = i.question_set.all().get(question_change_time=i.current_version)
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
                nodes.append(j.id)
            question_info = serializer.data
            question_info['id'] = question.id
            question_info['parents_node'] = nodes
            response.append(question_info)
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
            parents.append(KnowlegdeNodeSerializer(node).data)

        bank = node.question_bank

        group_data = {}
        group_data['current_version'] = post_data['question_change_time']
        group_data['belong_bank'] = QuestionBankSerializer(bank).data
        group_data['parents_node'] = parents

        q_group = QuestionGroupSerializer(data=group_data)

        if q_group.is_valid():
            new_group = q_group.save()
            new_group.belong_bank = bank
            post_data['history_version_id'] = new_group.id
        else:
            return Response(q_group.errors, status=400)

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
            return Response(response, status=201)
        return Response(question.errors, status=400)
