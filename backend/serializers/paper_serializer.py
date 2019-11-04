""" Serializers for Paper, Section and QuestionVersion"""
from rest_framework import serializers

from backend.models.paper import Paper
from backend.models.paper import Section


class PaperSerializer(serializers.ModelSerializer):
    """Serializer for QuestionGroup
    Attributes:
        id: The identity number of QuestionGroup
        current_version: The latest version's change time
        parents_node: This QuestionGroup belongs to KnowledgeNode with its id<int> in parents_node
        belong_bank: This QuestionGroup belongs ot QuestionBank with id=belong_bank
    """
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(allow_blank=True)
    title = serializers.CharField(allow_blank=True)
    tips = serializers.ListField(child=serializers.CharField(allow_blank=True))

    class Meta:
        model = Paper
        fields = [
            "id",
            "name",
            "title",
            "tips",
            "status",
        ]

    def create(self, validated_data):
        new_paper = Paper.objects.create(**validated_data)
        return new_paper

    def update(self, instance, validated_data):
        pass


class SectionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(allow_blank=True)
    title = serializers.CharField(allow_blank=True)

    class Meta:
        model = Section
        fields = [
            "id",
            "name",
            "title",
            "total_point",
            "section_num",
        ]

    def create(self, validated_data):
        return new_section

    def update(self, instance, validated_data):
        pass
