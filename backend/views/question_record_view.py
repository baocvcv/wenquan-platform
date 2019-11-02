""" QuestionRecord View """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from django.utils import timezone
from django.http import Http404

from backend.models import QuestionRecord
from backend.serializers import QuestionRecordSerializer

class QuestionRecordList(generics.ListAPIView):
    "Create and retrieve question records"
    queryset = QuestionRecord.objects.all()
    serializer_class = QuestionRecordSerializer

    def post(self, request):
        "Create a record"
        serializer = QuestionRecordSerializer(data=request.data)
        if serializer.is_valid():
            record = serializer.save()
            if record:
                record.judge()
                data = QuestionRecordSerializer(record)
                return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionRecordDetail(generics.RetrieveAPIView):
    "Retrieve detail info of a record"
    queryset = QuestionRecord.objects.all()
    serializer_class = QuestionRecordSerializer
