""" Serializers for QuestionBank """
from rest_framework import serializers
from django.utils.timezone import timezone

from backend.models.question_bank import QuestionBank


class QuestionBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionBank
        fields = [
            'id',
            "root_id",
            "name",
            "picture"
            "brief",
            "createTime",
            "lastUpdate",
            "authority",
            "question_count",
            "invitation_code_count",
            "activated_code_count",
        ]

    def create(self, validated_data):
        """create a question bank"""
        post_data = validated_data
        post_data.pop('id')
        post_data['createTime'] = timezone.now()
        post_data['lastUpdate'] = post_data['createTime']
        post_data['question_count'] = 0
        post_data['activated_code_count'] = 0
        question_bank = QuestionBank.objects.create(**post_data)
        question_bank.save()
        return question_bank

    def update(self, instance, validated_data):
        """update question group"""
        instance.root_id = validated_data.get('root_id', instance.root_id)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
