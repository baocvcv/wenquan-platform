""" Serializers for users """
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from backend.models.user_base import Admin, SuperAdmin, Student

from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
class StudentSerializer(serializers.ModelSerializer):
    """ Serializer for Student model """
    
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
        fields = ('email', 'username', 'password')
