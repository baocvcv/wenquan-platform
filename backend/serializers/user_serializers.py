""" Serializers for users """
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from backend.models import User
from backend.models import UserPermissions

class UserPermissionsSerializer(serializers.ModelSerializer):
    """ Serializer for usertype """
    is_student = serializers.BooleanField(default=True)
    is_admin = serializers.BooleanField(default=False)
    is_superadmin = serializers.BooleanField(default=False)
    can_view_students = serializers.BooleanField(default=False)
    can_edit_students = serializers.BooleanField(default=False)
    can_view_admins = serializers.BooleanField(default=False)
    can_edit_admins = serializers.BooleanField(default=False)

    class Meta:
        model = UserPermissions
        fields = ['is_student', 'is_admin', 'is_superadmin',
                  'can_view_students', 'can_edit_students',
                  'can_view_admins', 'can_edit_admins',]

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for User model """
    user_permissions = UserPermissionsSerializer(
        # default={
        #     'is_student':True,
        #     'is_admin': False,
        #     'is_superadmin': False,
        # }
    )

    def create(self, validated_data):
        """ create user """
        type_data = validated_data.pop('user_permissions')
        user_type = UserPermissions.objects.create(**type_data)
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            user_type=user_type,
        )
        user.set_password(validated_data['user']['password'])
        user.save()
        return user
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'user_permissions']
        read_only_fields = ['password']

# class StudentSerializer(serializers.ModelSerializer):
#     """ Serializer for Student model """
#     username = serializers.CharField(source='user.username')
#     email = serializers.EmailField(source='user.email')
#     password = serializers.CharField(source='user.password')
#     is_banned = serializers.BooleanField(default=False)
    
#     def create(self, validated_data):
#         """ create student """
#         #TODO: add email authentication method
#         user_type = UserType.objects.create(
#             is_student=True,
#             is_admin=False,
#             is_superadmin=False
#         )
#         user = User.objects.create_user(
#             user_type=user_type,
#             username=validated_data['user']['username'],
#             email=validated_data['user']['email'],
#         )
#         user.set_password(validated_data['user']['password'])
#         user.save()
#         student = Student(
#             user=user,
#             school_name="Tsinghua University",
#         )
#         student.save()
#         return student
#     class Meta:
#         """ meta """
#         model = Student
#         fields = ('id', 'email', 'username', 'password', 'is_banned')
