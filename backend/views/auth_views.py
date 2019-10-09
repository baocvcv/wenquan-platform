""" Authentication view """
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from backend.models.user_base import User
class CustomAuthToken(ObtainAuthToken):
    """ Custom auth backend"""
    def post(self, request, *args, **kwargs):
        """ get auth token """
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'password': user.password,
            'type':{
                'is_student': user.is_student,
                'is_admin': user.is_admin,
                'is_superadmin': user.is_superadmin
            }
        })
