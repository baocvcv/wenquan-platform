""" Serializers for Questions """
from rest_framework import serializers
from django.http import Http404

from backend.models.questions import BriefAnswerQ
from backend.models.questions import SingleChoiceQ
from backend.models.questions import MultpChoiceQ
from backend.models.questions import FillBlankQ
from backend.models.questions import TrueOrFalseQ
from backend.models.questions import QuestionGroup


def get_object(group_id):
    try:
        group = QuestionGroup.objects.get(id=group_id)
    except QuestionGroup.DoesNotExist:
        raise Http404
    return group


class SingleChoiceQSerializer(serializers.ModelSerializer):
    """Serializer for SingleChoiceQ"""
    history_version_id = serializers.IntegerField()
    id = serializers.IntegerField(required=False)
    question_image = serializers.ListField(child=serializers.CharField(allow_blank=True))
    question_name = serializers.CharField(allow_blank=True)

    class Meta:
        """Meta class"""
        model = SingleChoiceQ
        fields = [
            'id',
            'history_version_id',
            'question_name',
            'question_type',
            'question_level',
            'question_change_time',
            'question_content',
            'question_choice',
            'question_image',
            'question_ans',
            'question_solution',
        ]

    def create(self, validated_data):
        """create single choice question"""
        group = get_object(validated_data['history_version_id'])
        question = SingleChoiceQ.objects.create(
            **validated_data,
            history_version=group,
        )
        question.save()
        return question


class MultpChoiceQSerializer(serializers.ModelSerializer):
    """Serializer for MultpChoiceQ"""
    history_version_id = serializers.IntegerField()
    id = serializers.IntegerField(required=False)
    question_image = serializers.ListField(child=serializers.CharField(allow_blank=True))
    question_name = serializers.CharField(allow_blank=True)

    class Meta:
        """Meta class"""
        model = MultpChoiceQ
        fields = [
            'id',
            'history_version_id',
            'question_name',
            'question_type',
            'question_level',
            'question_change_time',
            'question_content',
            'question_choice',
            'question_image',
            'question_ans',
            'question_ans_num',
            'question_solution',
        ]

    def create(self, validated_data):
        """create multiple choices question"""
        group = get_object(validated_data['history_version_id'])
        question = MultpChoiceQ.objects.create(
            **validated_data,
            history_version=group,
        )
        question.save()
        return question


class TrueOrFalseQSerializer(serializers.ModelSerializer):
    """Serializer for TrueOrFalseQ"""
    history_version_id = serializers.IntegerField()
    id = serializers.IntegerField(required=False)
    question_image = serializers.ListField(child=serializers.CharField(allow_blank=True))
    question_name = serializers.CharField(allow_blank=True)

    class Meta:
        """Meta class"""
        model = TrueOrFalseQ
        fields = [
            'id',
            'history_version_id',
            'question_name',
            'question_type',
            'question_level',
            'question_change_time',
            'question_content',
            'question_image',
            'question_ans',
            'question_solution',
        ]

    def create(self, validated_data):
        """create true or false choices question"""
        group = get_object(validated_data['history_version_id'])
        question = TrueOrFalseQ.objects.create(
            **validated_data,
            history_version=group,
        )
        question.save()
        return question


class FillBlankQSerializer(serializers.ModelSerializer):
    """Serializer for FillBlankQ"""
    history_version_id = serializers.IntegerField()
    id = serializers.IntegerField(required=False)
    question_image = serializers.ListField(child=serializers.CharField(allow_blank=True))
    question_content = serializers.ListField(child=serializers.CharField(allow_blank=True))
    question_name = serializers.CharField(allow_blank=True)

    class Meta:
        """meta class"""
        model = FillBlankQ
        fields = [
            'id',
            'history_version_id',
            'question_name',
            'question_type',
            'question_level',
            'question_change_time',
            'question_content',
            'question_blank_num',
            'question_image',
            'question_ans',
            'question_solution',
        ]
        extra_kwargs = {
            "question_name": {
                "default": "Unnamed Question"
            },
            "question_image": {
                "allow_blank": True
            },
        }

    def create(self, validated_data):
        """create fill blank question"""
        group = get_object(validated_data['history_version_id'])
        question = FillBlankQ.objects.create(
            **validated_data,
            history_version=group,
        )
        question.save()
        return question


class BriefAnswerQSerializer(serializers.ModelSerializer):
    """Serializer for BriefAnswerQ"""
    history_version_id = serializers.IntegerField()
    id = serializers.IntegerField(required=False)
    question_image = serializers.ListField(child=serializers.CharField(allow_blank=True))
    question_name = serializers.CharField(allow_blank=True)

    class Meta:
        """meta class"""
        model = BriefAnswerQ
        fields = [
            'id',
            'history_version_id',
            'question_name',
            'question_type',
            'question_level',
            'question_change_time',
            'question_content',
            'question_image',
            'question_ans',
            'question_solution',
        ]

    def create(self, validated_data):
        """create brief answer question"""
        group = get_object(validated_data['history_version_id'])
        question = BriefAnswerQ.objects.create(
            **validated_data,
            history_version=group,
        )
        question.save()
        return question
