""" Authentication view """
from django.utils import timezone
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from ipware import get_client_ip

from backend.serializers import UserSerializer
from backend.models import User

class LoginView(KnoxLoginView):
    """ Custom auth backend"""
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        """ get auth token """
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # update user info
        user = serializer.validated_data['user']
        user.last_login_time = timezone.now()
        user.last_login_ip = get_client_ip(request)[0]
        user.save()

        if not user.is_active:
            return Response({'non_field_errors': ['Account not activated']}, status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return super(LoginView, self).post(request, format=None)
