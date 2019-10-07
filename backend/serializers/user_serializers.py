""" Serializers for users """
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from backend.models.user_base import User
from backend.models.user_base import Admin
from backend.models.user_base import SuperAdmin
from backend.models.user_base import Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
class StudentSerializer(serializers.ModelSerializer):
    """ Serializer for Student model """
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')
    
    def create(self, validated_data):
        #TODO: add email authentication method
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        user.is_student = True
        user.save()
        student = Student(
            user=user,
            school_name="Tsinghua University",
        )
        student.save()
        return student
    class Meta:
        model = Student
        fields = ('email', 'username', 'password')
