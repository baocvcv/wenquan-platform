""" Serializers for Questions """
from rest_framework import serializers

from backend.models.questions import BriefAnswerQ
from backend.models.questions import SingleChoiceQ
from backend.models.questions import MultpChoiceQ
from backend.models.questions import FillBlankQ
from backend.models.questions import TrueOrFalseQ
from .question_group_serializer import QuestionGroupSerializer


class SingleChoiceQSerializer(serializers.ModelSerializer):
    """Serializer for SingleChoiceQ"""
    history_version = QuestionGroupSerializer(read_only=True)

    class Meta:
        """Meta class"""
        model = SingleChoiceQ
        fields = [
            'history_version',
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
        question = SingleChoiceQ.objects.create(**validated_data)
        question.save()


class MultpChoiceQSerializer(serializers.ModelSerializer):
    """Serializer for MultpChoiceQ"""
    history_version = QuestionGroupSerializer(read_only=True)

    class Meta:
        """Meta class"""
        model = MultpChoiceQ
        fields = [
            'history_version',
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

    def create(self, validated_d):
        """create multiple choices question"""
        question = MultpChoiceQ.objects.create(**validated_data)
        question.save()


class TrueOrFalseQSerializer(serializers.ModelSerializer):
    """Serializer for TrueOrFalseQ"""
    history_version = QuestionGroupSerializer(read_only=True)

    class Meta:
        """Meta class"""
        model = TrueOrFalseQ
        fields = [
            'history_version',
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

        question = TrueOrFalseQ.objects.create(**validated_data)
        question.save()


class FillBlankQSerializer(serializers.ModelSerializer):
    """Serializer for FillBlankQ"""
    history_version = QuestionGroupSerializer(read_only=True)

    class Meta:
        """meta class"""
        model = FillBlankQ
        fields = [
            'history_version',
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

    def create(self, validated_data):
        """create fill blank question"""
        question = FillBlankQ.objects.create(**validated_data)
        question.save()


class BriefAnswerQSerializer(serializers.ModelSerializer):
    """Serializer for BriefAnswerQ"""
    history_version = QuestionGroupSerializer(read_only=True)

    class Meta:
        """meta class"""
        model = BriefAnswerQ
        fields = [
            'history_version',
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
        question = BriefAnswerQ.objects.create(**validated_data)
        question.save()
