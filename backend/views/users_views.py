""" Views for users """
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from backend.models import User
from backend.serializers.user_serializers import UserSerializer
from backend.scripts.email_verification import create_email_verification_record

class OwnerOnly(permissions.BasePermission):
    "Owner only access"
    def has_permission(self, request, view):
        "general permission"
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        "object permission"
        if request.user.user_group == 'Admin' or request.user.user_group == 'SuperAdmin':
            return True
        if request.user == obj:
            return True
        return False

class UserList(APIView):
    """ Create and get Users """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """ get a list of users """
        if request.user.user_group == 'Student':
            return Response(status=status.HTTP_403_FORBIDDEN)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ create a user """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                if not request.user.is_anonymous:
                    if request.user.user_group != 'Student':
                        user.is_active = True
                        user.save()
                        json = UserSerializer(user).data
                        return Response(json, status=status.HTTP_201_CREATED)
                # send the email verificaton record
                create_email_verification_record(user)
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):  # pylint: disable=too-many-ancestors
    """ Get, update or delete a student """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [OwnerOnly]
