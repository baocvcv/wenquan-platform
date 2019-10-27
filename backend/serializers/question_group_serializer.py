""" Serializers for QuestionGroup """
from rest_framework import serializers


class QuestionGroupSerializer(serializers.Serializer):
    """Serializer for QuestionGroup
    Attributes:
        id: The identity number of QuestionGroup
        current_version: The latest version's change time
        parents_node: This QuestionGroup belongs to KnowledgeNode with its id<int> in parents_node
        belong_bank: This QuestionGroup belongs ot QuestionBank with id=belong_bank
    """
    id = serializers.IntegerField(required=False)
    current_version = serializers.DateTimeField()
    parents_node = serializers.ListField(child=serializers.IntegerField())
    belong_bank = serializers.IntegerField()

    def create(self, validated_data):
        return

    def update(self, instance, validated_data):
        return
