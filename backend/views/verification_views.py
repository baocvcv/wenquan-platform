""" Views for verification """
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from backend.models import User
from backend.models import EmailVerificationRecord
from backend.serializers import UserSerializer

class EmailVerificationView(APIView):
    """ Perform email verification """
    def post(self, request):
        ''' verify if code exists '''
        token = request.data['token']
        record = EmailVerificationRecord.objects.get(token=token)
        if record is None or record.is_valid is False:
            return Response(
                {"token": "Token does not exist"},
                status=status.HTTP_400_BAD_REQUEST)
        else:
            user = record.user
            json = {}
            if record.send_type == "register":
                json['type'] = 'activation'
            elif record.send_type == "forget":
                json['type'] = 'password_reset'
            return Response(json, status=status.HTTP_200_OK)

    def put(self, request):
        ''' make modifications '''
        token = request.data['token']
        record = EmailVerificationRecord.objects.get(token=token)
        if record is None or record.is_valid is False:
            return Response(
                {"token": "Token does not exist"},
                status=status.HTTP_400_BAD_REQUEST)
        else:
            user = record.user
            if record.send_type == "forget":
                user.set_password(request.data['password'])
            elif record.send_type == "register":
                user.is_active = True
            record.is_valid = False
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
