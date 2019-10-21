""" Authentication view """
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.utils import timezone

from backend.serializers import UserSerializer

class CustomAuthToken(ObtainAuthToken):
    """ Custom auth backend"""
    def post(self, request, *args, **kwargs):
        """ get auth token """
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user.last_login_time = timezone.now()
        # user.save(update_fields='last_login_time')
        user.save()

        user_serializer = UserSerializer(user)
        data = user_serializer.data
        token, _ = Token.objects.get_or_create(user=user)
        data['token'] = token.key
        return Response(data)
