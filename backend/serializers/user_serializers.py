""" Serializers for users """
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from backend.models.user_base import Admin, SuperAdmin, Student

class StudentSerializer(serializers.ModelSerializer):
    """ Serializer for Student model """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Student.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=Student.objects.all())]
    )
    password = serializers.CharField(min_length=8)
    
    def create(self, validated_data):
        #TODO: add email authentication method
        student = Student.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return student
    class Meta:
        model = Student
        fields = ('username', 'email', )
