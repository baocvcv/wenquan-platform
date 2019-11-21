""" Serializers for Question Record """
from rest_framework import serializers

from backend.models import QuestionRecord
from backend.models improt Question

class QuestionRecordSerializer(serializers.ModelSerializer):
    "Serializer for QuestionRecord"
    id = serializers.IntegerField(required=False)
    record_time = serializers.DateTimeField(required=False)
    score = serializers.ListField(required=False)
    is_correct = serializers.BooleanField(required=False)
    question_type = serializers.CharField(required=False)
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)
    correct_or_not = serializers.ListField(read_only=True)
    comment = serializers.CharField(read_only=True)

    def to_representation(self, instance):
        """Add points"""
        ret = super().to_representation(instance)
        q = Question.objects.get(pk=ret['question_id'])
        if q.question_type == 4:
            ret['question_blank_num'] = q.question_blank_num
        return ret

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
            'user_id',
            'username',
            'correct_or_not',
            'comment',
        ]
