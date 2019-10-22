""" Serializers for KnoledgeNode """
from rest_framework import serializers

from backend.models.knowledge_node import KnowledgeNode


class KnowlegdeNodeSerializer(serializers.ModelSerializer):
    question_bank = QuestionBankSerializer(readonly=True)
    subnodes = KnowlegdeNodeSerializer(readonly=True, many=True)

    class Meta:
        model = KnowledgeNode
        fields = [
            'id',
            'question_bank',
            'name',
            'subnodes',
        ]

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
