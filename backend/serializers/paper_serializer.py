""" Serializers for Paper, Section and QuestionVersion"""
from rest_framework import serializers

from backend.models.paper import Paper
from backend.models.paper import Section


class PaperSerializer(serializers.ModelSerializer):
    """Serializer for PaperSerializer
    Attributes:
    """
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(allow_blank=True)
    tips = serializers.CharField(allow_blank=True)

    class Meta:
        model = Paper
        fields = [
            "id",
            "title",
            "total_point",
            "tips",
            "status",
            "time_limit",
        ]

    def create(self, validated_data):
        """Create a Paper"""
        new_paper = Paper.objects.create(**validated_data)
        return new_paper

    def update(self, instance, validated_data):
        pass


class SectionSerializer(serializers.ModelSerializer):
    """
    Serializer for Section
    Attributes:
    """
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(allow_blank=True)

    class Meta:
        model = Section
        fields = [
            "id",
            "title",
            "total_point",
            "section_num",
        ]

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
