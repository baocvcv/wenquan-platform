""" Serializers for users """
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from backend.models import User
from backend.models import UserPermissions
from backend.models import Profile

class UserPermissionsSerializer(serializers.ModelSerializer):
    """ Serializer for usertype """
    class Meta:
        model = UserPermissions
        # fields = ['edit_students', 'view_students', 'create_students', 'ban_students',
        #           'promote_students', 'view_admins', 'create_admins', 'edit_admins',
        #           'ban_admins', ]
        exclude = ['group_name']

class ProfileSerializer(serializers.ModelSerializer):
    """ Serializer for user profile """
    class Meta:
        model = Profile
        fields = ['school_name']

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for User model """
    user_permissions = UserPermissionsSerializer(read_only=True)
    profile = ProfileSerializer(required=False)

    def create(self, validated_data):
        """ create user """
        user_group = validated_data['user_group']
        user_permissions = UserPermissions.objects.get(group_name=user_group)
        profile = Profile.objects.create()
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            user_group=user_group,
            profile=profile,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        """ update user """
        user_group = validated_data['user_group']
        if user_group != instance.user_group:
            instance.user_group = user_group
            permissions = UserPermissions.objects.get(group_name=user_group)
            instance.user_permissions = permissions

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.is_banned = validated_data.get('is_banned', instance.is_banned)
        instance.save()

        profile_data = validated_data.pop('profile')
        profile = instance.profile
        profile.update(**profile_data)

        return instance
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password',
                  'last_login_time', 'last_login_ip', 'is_banned',
                  'user_type', 'user_permissions', 'profile']
        read_only_fields = ['password', 'last_login_time', 'last_login_ip']

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
