""" Views for users """
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.serializers.user_serializers import StudentSerializer

from backend.models.user_base import Admin, SuperAdmin, Student

#TODO: show

#TODO: register
class StudentCreate(APIView):
    """ Creates the student """

    def post(self, request, format='json'):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            if student:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        

#TODO: activate

#TODO: login?