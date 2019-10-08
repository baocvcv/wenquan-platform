""" Views for users """
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import Http404

from backend.models.user_base import User
from backend.serializers.user_serializers import StudentSerializer
from backend.models.user_base import Admin, SuperAdmin, Student

from backend.serializers.user_serializers import UserSerializer

class StudentList(APIView):
    """ Creates the student """

    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format='json'):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            if student:
                token = Token.objects.create(user=student.user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Get, update or delete a student """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer