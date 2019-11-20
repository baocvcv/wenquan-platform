""" Views for verification """
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from backend.scripts.email_verification import create_email_verification_record
from backend.scripts.email_verification import use_token

class EmailVerificationView(APIView):
    """ Perform email verification """
    permission_classes = (permissions.AllowAny, )

    def get(self, request):
        """ send verification email """
        user = request.user
        if not user.is_active:
            create_email_verification_record(user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """ make modifications """
        token = request.data['token']
        msg, sta = use_token(token)
        return Response(msg, sta)
