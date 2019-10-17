""" Questino view """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from backend.serializers.question_serializer import SingleChoiceQSerializer
from backend.serializers.question_serializer import MultpChoiceQSerializer
from backend.serializers.question_serializer import TrueOrFalseQSerializer
from backend.serializers.question_serializer import FillBlankQSerializer
from backend.serializers.question_serializer import BriefAnswerQSerializer

from backend.models.questions import QuestionGroup
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

            serializer.parents_node = []
            for j in i.parents_node.all():
                serializer.parents_node += j.id
            response += serializer.data
        return Response(response)

    def post(self, request):
        """Create a question"""
        question = JSONParser().parse(request)
        qtype = question['question_type']

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

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
