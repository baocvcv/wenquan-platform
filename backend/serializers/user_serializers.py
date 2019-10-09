""" Serializers for users """
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from backend.models.user_base import User
from backend.models.user_base import Admin
from backend.models.user_base import SuperAdmin
from backend.models.user_base import Student

class StudentSerializer(serializers.ModelSerializer):
    """ Serializer for Student model """
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')
    is_banned = serializers.BooleanField(source='user.is_banned', default=False)
    
    def create(self, validated_data):
        """ create student """
        #TODO: add email authentication method
        user = User(
            username=validated_data['user']['username'],
            email=validated_data['user']['email'],
        )
        user.is_student = True
        user.set_password(validated_data['user']['password'])
        user.save()
        student = Student(
            user=user,
            school_name="Tsinghua University",
        )
        student.save()
        return student
    class Meta:
        """ meta """
        model = Student
        fields = ('email', 'username', 'password', 'is_banned')

class AdminSerializer(serializers.ModelSerializer):
    """ Serializer for Admin model """
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')
    is_banned = serializers.BooleanField(source='user.is_banned', default=False)
    
    def create(self, validated_data):
        """ create admin """
        user = User(
            username=validated_data['user']['username'],
            email=validated_data['user']['email'],
        )
        user.is_student = True
        user.is_staff = True
        user.set_password(validated_data['user']['password'])
        user.save()
        admin = Admin(user=user)
        admin.save()
        return admin 
    class Meta:
        """ meta """
        model = Admin 
        fields = ('email', 'username', 'password', 'is_banned')

class SuperAdminSerializer(serializers.ModelSerializer):
    """ Serializer for SuperAdmin model """
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')
    
    def create(self, validated_data):
        """ create super admin """
        user = User(
            username=validated_data['user']['username'],
            email=validated_data['user']['email'],
        )
        user.is_student = True
        user.is_staff = True
        user.is_superadmin = True
        user.set_password(validated_data['user']['password'])
        user.save()
        superadmin = SuperAdmin(user=user)
        superadmin.save()
        return superadmin 
    class Meta:
        """ meta"""
        model = SuperAdmin 
        fields = ('email', 'username', 'password')