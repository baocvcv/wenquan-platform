""" PaperRecord View """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from django.utils import timezone
from django.http import Http404

from backend.models import QuestionRecord
from backend.models import PaperRecord
from backend.models import Paper
from backend.serializers import QuestionRecordSerializer
from backend.serializers import PaperRecordSerializer

class PaperRecordList(generics.ListAPIView):
    "Create and retrieve paper record"
    queryset = PaperRecord.objects.all()
    serializer_class = PaperRecordSerializer

class PaperRecordDetail(generics.RetrieveAPIView):
    "Update and retrieve paper record"
    queryset = PaperRecord.objects.all()
    serializer_class = PaperRecordSerializer

    def post(self, request, pk):
        " Update paper record "
        paper_record = PaperRecord.objects.get(id=pk)
        if not paper_record.can_update():
            return Response(
                {"error": "Paper no longer active."},
                status=status.HTTP_400_BAD_REQUEST,
                )
        # paper = Paper.objects.get(id=request.data['paper_id'])
        # sections = paper.section_set.all()
        section_data = request.data['sections']
        for data in section_data:
            question_data = data['questions']
            question_record = QuestionRecord(
                question_id=question_data['question_id'],
                paper_record=paper_record,
            )
            question_record.set_ans(question_data['ans'])
            question_record.save()
        return Response(status=status.HTTP_200_OK)


    def put(self, request, pk):
        " Stop answering paper "
        paper_record = PaperRecord.objects.get(id=pk)
        cmd = request.data['action']
        if cmd == 'pause':
            paper_record.is_active = False
        elif cmd == 'continue':
            paper_record.is_active = True
        elif cmd == 'finish':
            paper_record.is_active = False
            paper_record.time_left = 0
