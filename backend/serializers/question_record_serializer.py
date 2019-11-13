""" Serializers for Question Record """
from rest_framework import serializers

from backend.models import QuestionRecord

class QuestionRecordSerializer(serializers.ModelSerializer):
    "Serializer for QuestionRecord"
    id = serializers.IntegerField(required=False)
    record_time = serializers.DateTimeField(required=False)
    score = serializers.ListField(required=False)
    is_correct = serializers.BooleanField(required=False)
    question_type = serializers.CharField(required=False)
    owner = serializers.IntegerField(source="user.id", read_only=True)


    class Meta:
        "Meta"
        model = QuestionRecord
        fields = [
            'id',
            'question_id',
            'question_type',
            'record_time',
            'ans',
            'score',
            'is_correct',
            'owner',
        ]
