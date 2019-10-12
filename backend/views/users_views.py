""" Views for users """
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
# from django.http import Http404

from backend.models.user_base import User
from backend.models.user_base import Admin
from backend.models.user_base import Student
# from backend.models.user_base import SuperAdmin

from backend.serializers.user_serializers import UserSerializer
from backend.serializers.user_serializers import StudentSerializer
from backend.serializers.user_serializers import AdminSerializer
# from backend.serializers.user_serializers import SuperAdminSerializer

class UserList(APIView):
    """ Create and get Users """

    def get(self, request):
        """ get a list of users """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ create a user """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveUpdateDestroyAPIView): # pylint: disable=too-many-ancestors
    """ Get, update or delete a student """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentList(APIView):
    """ Creates the student """

    def get(self, request):
        """ get a list of students """
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ create a user """
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            if student:
                token = Token.objects.create(user=student.user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(generics.RetrieveUpdateDestroyAPIView): # pylint: disable=too-many-ancestors
    """ Get, update or delete a student """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class AdminList(APIView):
    """ Creates the Admin """

    def get(self, request):
        """ get a list of admins """
        admins = Admin.objects.all()
        serializer = AdminSerializer(admins, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ create an admin """
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            admin = serializer.save()
            if admin:
                token = Token.objects.create(user=admin.user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminDetail(generics.RetrieveUpdateDestroyAPIView): # pylint: disable=too-many-ancestors
    """ Retrieve, modify or delete admin """
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
