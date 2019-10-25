""" Views for verification """
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

# from backend.models import User
from backend.models import EmailVerificationRecord
from backend.serializers import UserSerializer
from backend.scripts.email_verification import create_email_verification_record

#TODO: split password change from this
class EmailVerificationView(APIView):
    """ Perform email verification """
    def get(self, request):
        """ send verification email """
        user = request.user
        if user.is_active == False:
            create_email_verification_record(user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """ make modifications """
        token = request.data['token']
        record = EmailVerificationRecord.objects.get(token=token)
        if record is None or record.is_valid is False:
            return Response(
                {"token": "Token does not exist"},
                status=status.HTTP_400_BAD_REQUEST)
        user = record.user
        if record.send_type == "register":
            if record.is_time_valid(timezone.now()):
                user.is_active = True
                user.save()
                record.is_valid = False
                record.save()
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"Error": "Token has expired!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "Wrong url!"}, status=status.HTTP_400_BAD_REQUEST)
