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

    def create(self, validated_data):
        """create question group"""
        node = KnowledgeNode(**validated_data)
        node.save()
        return node

    def update(self, instance, validated_data):
        instance.question_bank = validated_data.get('question_bank', instance.question_bank)
        instance.name = validated_data.get('name', instance.name)
        instance.subnodes = validated_data.get('subnodes', instance.subnodes)
        instance.save()
        return instance
