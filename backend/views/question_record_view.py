""" QuestionRecord View """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from django.utils import timezone
from django.http import Http404

from backend.models.questions import Question
from backend.models import QuestionRecord
from backend.serializers import QuestionRecordSerializer

class QuestionRecordList(generics.ListAPIView):
    "Create and retrieve question records"
    queryset = QuestionRecord.objects.all()
    serializer_class = QuestionRecordSerializer

    def post(self, request):
        "Create a record"
        data = request.data
        # judge
        question = Question.objects.get(id=data['question_id'])
        is_correct, _ = question.checker(data['ans'])
        # add record
        record = QuestionRecord(
            question_id=data['question_id'],
            questions_type=data['question_type'],
            is_correct=is_correct,
            score=-1,
        )
        record.set_ans(data['ans'])
        if record.save():
            data = QuestionRecordSerializer(record)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(
            {'error': 'Error saving the record'},
            status=status.HTTP_400_BAD_REQUEST
        )

class QuestionRecordDetail(generics.RetrieveAPIView):
    "Retrieve detail info of a record"
    queryset = QuestionRecord.objects.all()
    serializer_class = QuestionRecordSerializer
