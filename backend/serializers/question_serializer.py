""" Serializers for Questions """
import datetime
from rest_framework import serializers

from backend.models import QuestionGroup
from backend.models.questions import BriefAnswerQ
from backend.models.questions import SingleChoiceQ
from backend.models.questions import MultpChoiceQ
from backend.models.questions import FillBlankQ
from backend.models.questions import TrueOrFalseQ


class BriefAnswerQSerializer(serializers.ModelSerializer):
    """Serializer for BriefAnswerQ"""
    class Meta:
        """meta class"""
        model = BriefAnswerQ
        fields = [
            'history_version',
            'question_id',
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

        new_q = {}
        new_group = QuestionGroup.objects.create(current_version=datetime.datetime.now())
        new_q['history_version'] = new_group
        new_q['question_id'] = new_group.id
        new_q['question_name'] = validated_data['name']
        new_q['question_type'] = validated_data['type']
        new_q['level'] = validated_data['level']
        new_q['question_change_time'] = new_group.current_version
        new_q['question_content'] = validated_data['content']
        new_q['question_image'] = validated_data['image']
        new_q['question_ans'] = validated_data['ans']
        new_q['question_solution'] = validated_data['solution']
        question = BriefAnswerQ.objects.create(**new_q)
        question.save()

    def update(self, instance, validated_data):
        """
        update a question,
        create a new instance related to same QuestionGroup
        """
        new_q = {}
        instance.history_version.update(current_version=datetime.datetime.now())
        new_q['history_version'] = instance.history_version
        new_q['question_id'] = instance.question_id
        new_q['question_name'] = validated_data['name']
        new_q['level'] = validated_data['level']
        new_q['question_change_time'] = instance.history_version.current_version
        new_q['question_content'] = validated_data['content']
        new_q['question_image'] = validated_data['image']
        new_q['question_ans'] = validated_data['ans']
        new_q['question_solution'] = validated_data['solution']
        question = BriefAnswerQ.objects.create(**new_q)
        question.save()
