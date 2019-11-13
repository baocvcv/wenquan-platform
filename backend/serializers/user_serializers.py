""" Serializers for users """
from rest_framework import serializers

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
    is_banned = serializers.BooleanField(default=False)
    user_group = serializers.CharField(default="Student")
    password = serializers.CharField(required=False)
    question_banks = serializers.ListField(required=False)

    def create(self, validated_data):
        """ create user """
        user_permissions = UserPermissions.objects.get(group_name="Student")
        if 'profile' in validated_data:
            profile_data = validated_data.pop('profile')
            profile = Profile.objects.create(**profile_data)
        else:
            profile = Profile.objects.create()
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            user_group="Student",
            profile=profile,
            user_permissions=user_permissions,
            is_active=False,
            question_banks=[],
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
        # NEED to be changed for better permission control
        instance.question_banks = validated_data.get('question_banks', instance.question_banks)
        instance.save()

        if 'profile' in validated_data:
            profile_data = validated_data.pop('profile')
            profile = instance.profile
            profile_serializer = ProfileSerializer(data=profile_data)
            profile_serializer.update(profile, profile_data)

        return instance

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password',
                  'last_login_time', 'last_login_ip', 'is_banned', 'is_active',
                  'user_group', 'user_permissions', 'profile', 'question_banks']
        read_only_fields = ['last_login_time', 'last_login_ip',]
