""" Serializers for KnoledgeNode """
from rest_framework import serializers

from backend.models.knowledge_node import KnowledgeNode
from .question_bank_serializer import QuestionBankSerializer


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class KnowlegdeNodeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    question_bank = QuestionBankSerializer(read_only=True)
    subnodes = RecursiveField(many=True, required=False)

    class Meta:
        model = KnowledgeNode
        fields = [
            'id',
            'question_bank',
            'name',
            'subnodes',
        ]
        extra_kwargs = {
            "name": {
                "required": False
            },
        }
