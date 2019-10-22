""" Serializers for QuestionBank """
from rest_framework import serializers

from backend.models.question_bank import QuestionBank


class QuestionBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionBank
        fields = [
            'id',
            'root_id',
            'name',
        ]

    def create(self, validated_data):
        """create a question bank"""
        question_bank = QuestionBank.objects.create(**validated_data)
        question_bank.save()

    def update(self, instance, validated_data):
        """create question group"""
        instance.root_id = validated_data.get('root_id', instance.root_id)
        instance.name = validated_data.get('name', instance.name)
        question_bank.save()
