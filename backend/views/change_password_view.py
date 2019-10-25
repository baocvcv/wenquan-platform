""" Views for password change"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

# from backend.models import User
from backend.models import EmailVerificationRecord
from backend.serializers import UserSerializer
from backend.scripts.email_verification import create_email_verification_record

# TODO: change this
class ChangePasswordView(APIView):
    """ Handle password change """
    def get(self, request):
        """ send verification email """
        user = request.user
        create_email_verification_record(user, send_type='forget')
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        """ make modifications """
        token = request.data['token']
        record = EmailVerificationRecord.objects.get(token=token)
        if record is None or record.is_valid == False:
            return Response(
                {"token": "Token does not exist"},
                status=status.HTTP_400_BAD_REQUEST)
        user = record.user
        if record.send_type == "forget":
            if record.is_time_valid(timezone.now()):
                user.set_password(request.data['password'])
                user.save()
                record.is_valid = False
                record.save()
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"Error": "Token has expired!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "Wrong url!"}, status=status.HTTP_400_BAD_REQUEST)
