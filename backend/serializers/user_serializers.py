""" Serializers for users """
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from backend.models.user_base import UserType
from backend.models.user_base import User
from backend.models.user_base import Admin
from backend.models.user_base import SuperAdmin
from backend.models.user_base import Student

class UserTypeSerializer(serializers.ModelSerializer):
    """ Serializer for usertype """
    is_student = serializers.BooleanField(default=True)
    is_admin = serializers.BooleanField(default=False)
    is_superadmin = serializers.BooleanField(default=False)

    class Meta:
        model = UserType
        fields = ['is_student', 'is_admin', 'is_superadmin']

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for User model """
    user_type = UserTypeSerializer(
        default={
            'is_student':True,
            'is_admin': False,
            'is_superadmin': False,
        }
    )

    def create(self, validated_data):
        """ create user """
        type_data = validated_data.pop('user_type')
        user_type = UserType.objects.create(**type_data)
        user = User(
            user_type=user_type,
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        """ update user """
        type_data = validated_data.pop('user_type')
        user_type = instance.user_type

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.is_banned = validated_data.get('is_banned', instance.is_banned)
        instance.save()

        is_student = type_data.get('is_student', user_type.is_student)
        is_admin = type_data.get('is_admin', user_type.is_admin)
        is_superadmin = type_data.get('is_superadmin', user_type.is_superadmin)
        type_sum = is_student + is_admin + is_superadmin
        if type_sum != 1:
            return instance
        if user_type.is_student != is_student:
            if is_student:
                Student.objects.create(
                    user=instance,
                    school_name='Tsinghua'
                )
            else:
                instance.student.delete()
        if user_type.is_admin != is_admin:
            if is_admin:
                Admin.objects.create(user=instance)
            else:
                instance.admin.delete()
        if user_type.is_superadmin != is_superadmin:
            if is_superadmin:
                SuperAdmin.objects.create(user=instance)
            else:
                instance.superadmin.delete()

        user_type.is_student = is_student
        user_type.is_admin = is_admin
        user_type.is_superadmin = is_superadmin
        user_type.save()

        return instance
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'user_type', 'is_banned']
        read_only_fields = ['id', 'password']

class StudentSerializer(serializers.ModelSerializer):
    """ Serializer for Student model """
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')
    is_banned = serializers.BooleanField(source='user.is_banned', default=False)
    school_name = serializers.CharField(required=False)
    
    def create(self, validated_data):
        """ create student """
        #TODO: add email authentication method
        user_type = UserType.objects.create(
            is_student=True,
            is_admin=False,
            is_superadmin=False
        )
        user = User.objects.create_user(
            user_type=user_type,
            username=validated_data['user']['username'],
            email=validated_data['user']['email'],
        )
        user.set_password(validated_data['user']['password'])
        user.save()
        student = Student(
            user=user,
            school_name="Tsinghua University",
        )
        student.save()
        return student

    def update(self, instance, validated_data):
        """ update student """
        user_data = validated_data.pop('user')
        user = instance.user
        # update user
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.is_banned = user_data.get('is_banned', user.is_banned)
        user.save()
        # update student
        instance.school_name = validated_data.get('school_name', instance.school_name)
        instance.save()
        return instance
    class Meta:
        """ meta """
        model = Student
        fields = ['id', 'email', 'username', 'password', 'is_banned', 'school_name']
        read_only_fields = ['id', 'password']

class AdminSerializer(serializers.ModelSerializer):
    """ Serializer for Admin model """
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')
    is_banned = serializers.BooleanField(source='user.is_banned', default=False)
    
    def create(self, validated_data):
        """ create admin """
        user_type = UserType.objects.create(
            is_student=False,
            is_admin=True,
            is_superadmin=False
        )
        user = User(
            user_type=user_type,
            username=validated_data['user']['username'],
            email=validated_data['user']['email'],
        )
        user.set_password(validated_data['user']['password'])
        user.save()
        admin = Admin(user=user)
        admin.save()
        return admin 

    def update(self, instance, validated_data):
        """ update student """
        user_data = validated_data.pop('user')
        user = instance.user
        # update user
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.is_banned = user_data.get('is_banned', user.is_banned)
        user.save()
        # update admin
        instance.save()
        return instance

    class Meta:
        """ meta """
        model = Admin 
        fields = ['id', 'email', 'username', 'password', 'is_banned']
        read_only_fields = ['id', 'password']

class SuperAdminSerializer(serializers.ModelSerializer):
    """ Serializer for SuperAdmin model """
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')
    is_banned = serializers.BooleanField(source='user.is_banned', default=False)
    
    def create(self, validated_data):
        """ create super admin """
        user_type = UserType.objects.create(
            is_student=True,
            is_admin=False,
            is_superadmin=False
        )
        user = User(
            user_type=user_type,
            username=validated_data['user']['username'],
            email=validated_data['user']['email'],
        )
        user.set_password(validated_data['user']['password'])
        user.save()
        superadmin = SuperAdmin(user=user)
        superadmin.save()
        return superadmin 

    def update(self, instance, validated_data):
        """ update student """
        user_data = validated_data.pop('user')
        user = instance.user
        # update user
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.is_banned = user_data.get('is_banned', user.is_banned)
        user.save()
        # update superadmin
        instance.save()
        return instance

    class Meta:
        """ meta"""
        model = SuperAdmin 
        fields = ['id', 'email', 'username', 'password', 'is_banned']
        read_only_fields = ['id', 'password']