""" Serializers for Questions """
import datetime
from rest_framework import serializers

from backend.models import QuestionGroup
from backend.models.questions import BriefAnswerQ
from backend.models.questions import SingleChoiceQ
from backend.models.questions import MultpChoiceQ
from backend.models.questions import FillBlankQ
from backend.models.questions import TrueOrFalseQ


def create_pre_task(validated_data):
    """
    tasks related to QuestionBanks
    should be done before creating
    """
    new_group = QuestionGroup.objects.create(current_version=datetime.datetime.now())
    node_id = validated_data.pop("parents_node")
    for i in node_id:
        node = KnowledgeNode.objects.get(id=i)
        new_group.parents_node.add(node)
    new_group.save()
    node.question_bank.questions.add(new_group)
    return new_group


def update_pre_task(instance, validated_data):
    """
    tasks related to QuestionBanks
    should be done before upadating
    """
    this_group = instance.history_version
    now_parents_node = this_group.parents_node
    new_node_id = validated_data.pop("knowledge_node")
    now_parents_node.clear()
    for i in new_node_id:
        node = KnowledgeNode.objects.get(id=i)
        now_parents_node.add(node)
    this_group.current_version = datetime.datetime.now()


class SingleChoiceQSerializer(serializers.ModelSerializer):
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
        create_pre_task(validated_data)
        question = SingleChoiceQ.objects.create(
            history_version=new_group,
            question_change_time=datetime.datetime.now(),
            **new_q,
        )
        question.save()
        new_group.save()
        node.question_bank.questions.add(question)

    def update(self, instance, validated_data):
        """
        update a question,
        create a new instance related to same QuestionGroup
        """
        update_pre_task(instance, validated_data)
        question = SingleChoiceQ.objects.create(
            history_version=instance.history_version,
            question_change_time=this_group.current_version,
            **validated_data,
        )
        question.save()


class MultpChoiceQSerializer(serializers.ModelSerializer):
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

    def create(self, validated_data):
        """create multiple choices question"""
        create_pre_task(validated_data)
        question = MultpChoiceQ.objects.create(
            history_version=new_group,
            question_change_time=datetime.datetime.now(),
            **new_q,
        )
        question.save()
        new_group.save()
        node.question_bank.questions.add(question)

    def update(self, instance, validated_data):
        """
        update a question,
        create a new instance related to same QuestionGroup
        """
        update_pre_task(instance, validated_data)
        question = MultpChoiceQ.objects.create(
            history_version=instance.history_version,
            question_change_time=this_group.current_version,
            **validated_data,
        )
        question.save()


class TrueOrFalseQSerializer(serializers.ModelSerializer):
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
        create_pre_task(validated_data)
        question = TrueOrFalseQ.objects.create(
            history_version=new_group,
            question_change_time=datetime.datetime.now(),
            **new_q,
        )
        question.save()
        new_group.save()
        node.question_bank.questions.add(question)

    def update(self, instance, validated_data):
        """
        update a question,
        create a new instance related to same QuestionGroup
        """
        update_pre_task(instance, validated_data)
        question = TrueOrFalseQ.objects.create(
            history_version=instance.history_version,
            question_change_time=this_group.current_version,
            **validated_data,
        )
        question.save()


class FillBlankQSerializer(serializers.ModelSerializer):
    """Serializer for FillBlankQ"""
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
        new_group = create_pre_task(validated_data)
        question = FillBlankQ.objects.create(
            history_version=new_group,
            question_change_time=datetime.datetime.now(),
            **new_q,
        )
        question.save()

    def update(self, instance, validated_data):
        """
        update a question,
        create a new instance related to same QuestionGroup
        """
        update_pre_task(instance, validated_data)
        question = FillBlankQ.objects.create(
            history_version=instance.history_version,
            question_change_time=instance.history_version.get().current_version,
            **validated_data,
        )
        question.save()


class BriefAnswerQSerializer(serializers.ModelSerializer):
    """Serializer for BriefAnswerQ"""
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
        new_group = create_pre_task(validated_data)
        question = BriefAnswerQ.objects.create(
            history_version=new_group,
            question_change_time=datetime.datetime.now(),
            **new_q,
        )
        question.save()

    def update(self, instance, validated_data):
        """
        update a question,
        create a new instance related to same QuestionGroup
        """
        update_pre_task(instance, validated_data)
        question = BriefAnswerQ.objects.create(
            history_version=instance.history_version,
            question_change_time=instance.history_version.get().current_version,
            **validated_data,
        )
        question.save()
