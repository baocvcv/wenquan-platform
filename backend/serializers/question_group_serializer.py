""" Serializers for QuestionGroup """
from rest_framework import serializers

from backend.models.question_bank import QuestionBank
from backend.models.questions import QuestionGroup
from .knowledge_node_serializer import KnowlegdeNodeSerializer
from .question_bank_serializer import QuestionBankSerializer
from backend.models.knowledge_node import KnowledgeNode


class QuestionGroupSerializer(serializers.ModelSerializer):
    belong_bank = QuestionBankSerializer(required=False)
    parents_node = KnowlegdeNodeSerializer(many=True)
    id = serializers.IntegerField(required=False)

    class Meta:
        model = QuestionGroup
        fields = [
            'id',
            'current_version',
            'parents_node',
            'belong_bank',
        ]

    def create(self, validated_data):
        """create question group"""

        bank = QuestionBank.objects.get(id=validated_data['belong_bank']['id'])
        nodes = []
        for i in validated_data['parents_node']:
            nodes.append(KnowledgeNode.objects.get(id=i['id']))
        new_group = QuestionGroup.objects.create(
            current_version=validated_data['current_version'],
            belong_bank=bank,
        )
        new_group.parents_node.set(nodes)
        new_group.belong_bank = bank
        new_group.save()
        return new_group

    def update(self, instance, validated_data):
        """create question group"""
        instance.current_version = validated_data.get('current_version', instance.current_version)
        instance.belong_bank = validated_data.get('belong_bank', instance.current_version)
        instance.parents_node = validated_data.get('parents_node', instance.current_version)
        instance.question_set = validated_data.get('question_set', instance.current_version)
        instance.save()
        return instance
