""" Serializers for QuestionGroup """
from rest_framework import serializers


class QuestionGroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    current_version = serializers.DateTimeField()
    parents_node = serializers.ListField(child=serializers.IntegerField())
    belong_bank = serializers.IntegerField()
