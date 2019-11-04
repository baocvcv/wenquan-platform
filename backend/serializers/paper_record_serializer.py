""" Serializers for Paper Record """
from rest_framework import serializers
from django.http import Http404

from backend.models import QuestionRecord

class PaperRecordSerializer(serializers.ModelSerializer):
    "Serializer for PaperRecord"
    pass