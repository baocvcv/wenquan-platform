""" Views for password change"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from backend.scripts.email_verification import create_email_verification_record
from backend.scripts.email_verification import use_token

class ChangePasswordView(APIView):
    """ Handle password change """
    def get(self, request):
        """ send verification email """
        user = request.user
        create_email_verification_record(user, send_type='forget')
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        """ change pasword """
        token = request.data['token']
        msg, sta = use_token(token, request.data['password'])
        return Response(msg, sta)
