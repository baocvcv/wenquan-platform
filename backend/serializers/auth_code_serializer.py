""" Serializer for auth code """
from rest_framework import serializers

from backend.models import AuthCode

class AuthCodeSerializer(serializers.ModelSerializer):
    "Serialzier for authcode, only used for unserializing"
    question_bank_id = serializers.IntegerField(source="question_bank.id")

    class Meta:
        model = AuthCode
        fields = ["key", "time_generated", "is_usable", "question_bank_id"]
        read_only_fields = ["time_generated", "is_usable", "question_bank_id"]
