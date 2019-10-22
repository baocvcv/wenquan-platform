""" Views for users """
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
# from django.http import Http404

from backend.models import User

from backend.serializers.user_serializers import UserSerializer


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


class UserDetail(generics.RetrieveUpdateDestroyAPIView):  # pylint: disable=too-many-ancestors
    """ Get, update or delete a student """
    queryset = User.objects.all()
    serializer_class = UserSerializer
