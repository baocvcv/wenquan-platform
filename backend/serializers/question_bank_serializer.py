""" Serializers for QuestionBank """
from rest_framework import serializers
from django.utils import timezone

from backend.models.question_bank import QuestionBank


class QuestionBankSerializer(serializers.ModelSerializer):
    """Serializer for QuestionBank
    Attributes:
        root_id: The id of root KnowledgeNode
        name: Name of bank
        picture: The url of banks icon
        brief: The brief introduction of bank
        createTime: The date and time when bank was created
        lastUpdate: The date and time of the latest modifying
        authority: The authority of bank
        question_count: The number of QuestionGroup related to bank
        invitation_code_count: The number of invitation code of bank
        activated_code_count: The number of activated invitation bank
    """
    class Meta:
        model = QuestionBank
        fields = [
            "root_id",
            "name",
            "picture",
            "brief",
            "authority",
            "createTime",
            "lastUpdate",
            "question_count",
            "activated_code_count",
            "invitation_code_count",
        ]
        extra_kwargs = {
            "question_count": {
                "required": False
            },
            "picture": {
                "allow_blank": True
            },
            "createTime": {
                "required": False
            },
            "lastUpdate": {
                "required": False
            },
            "activated_code_count": {
                "required": False
            },
        }

    def create(self, validated_data):
        """Create a question bank"""
        post_data = validated_data
        post_data['createTime'] = timezone.now()
        post_data['lastUpdate'] = post_data['createTime']
        post_data['question_count'] = 0
        post_data['activated_code_count'] = 0
        question_bank = QuestionBank.objects.create(**post_data)
        question_bank.save()
        return question_bank

    def update(self, instance, validated_data):
        """Update question group"""
        instance.root_id = validated_data.get('root_id', instance.root_id)
        instance.name = validated_data.get('name', instance.name)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.brief = validated_data.get('brief', instance.brief)
        instance.lastUpdate = timezone.now()
        instance.authority = validated_data.get('authority', instance.authority)

        instance.question_count = \
            validated_data.get('question_count', instance.question_count)
        instance.invitation_code_count = \
            validated_data.get('invitation_code_count', instance.invitation_code_count)
        instance.activated_code_count = \
            validated_data.get('activated_code_count', instance.activated_code_count)

        instance.save()
        return instance
