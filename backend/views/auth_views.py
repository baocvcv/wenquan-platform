""" Authentication view """
from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone
from ipware import get_client_ip
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.exceptions import TokenError

from backend.serializers import UserSerializer
from backend.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user_id'] = self.user.id
        data['username'] = self.user.username

        return data

class CustomAuthToken(TokenObtainPairView):
    """ Custom auth backend"""
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        """ get auth token """
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        print(serializer.validated_data)

        user_id = serializer.validated_data['user_id']
        user = User.objects.get(pk=user_id)
        user.last_login_time = timezone.now()
        user.last_login_ip = get_client_ip(request)[0]
        user.save()

        return Response(serializer.validated_data, status.HTTP_200_OK)
