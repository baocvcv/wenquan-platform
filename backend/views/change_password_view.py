""" Views for password change"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from backend.scripts.email_verification import create_email_verification_record
from backend.scripts.email_verification import use_token

from backend.serializers import UserSerializer
from backend.models import User

class ChangePasswordView(APIView):
    """ Handle password change """
    def post(self, request):
        """ send verification email """
        user = User.objects.get_by_natural_key(request.data['username'])
        create_email_verification_record(user, send_type='forget')
        return Response(status=status.HTTP_200_OK)

    def put(self, request):
        """ change pasword """
        data = request.data
        if 'token' in data:
            token = data['token']
            msg, sta = use_token(token, data['password'])
            return Response(msg, sta)
        user = request.user
        user.set_password(data['password'])
        user.save()
        return Response(UserSerializer(user).data, status.HTTP_200_OK)
