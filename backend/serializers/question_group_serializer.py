""" Serializers for QuestionGroup """
from rest_framework import serializers

from backend.models.questions import QuestionGroup
from .knowledge_node_serializer import KnowlegdeNodeSerializer


class QuestionGroupSerializer(serializers.ModelSerializer):
    parents_node = KnowlegdeNodeSerializer(many=True)
    belong_bank = QuestionBankSerializer()

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
        validated_data.pop('id')
        question_group = QuestionGroup.objects.create(**validated_data)
        question_group.save()
        return question_group

    def update(self, instance, validated_data):
        """create question group"""
        instance.current_version = validated_data.get('current_version', instance.current_version)
        instance.belong_bank = validated_data.get('belong_bank', instance.current_version)
        instance.parents_node = validated_data.get('parents_node', instance.current_version)
        instance.question_set = validated_data.get('question_set', instance.current_version)
        instance.save()
        return instance
