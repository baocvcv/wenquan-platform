""" PaperRecord View """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from django.utils import timezone
from django.http import Http404

from backend.models import QuestionRecord
from backend.serializers import QuestionRecordSerializer

class PaperRecordList(generics.ListAPIView):
    "Create and retrieve paper record"
    pass

class PaperRecordDetail(generics.RetrieveAPIView):
    "Update and retrieve paper record"
    pass