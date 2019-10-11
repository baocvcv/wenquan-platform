""" Authentication view """
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# from backend.models.user_base import User

class CustomAuthToken(ObtainAuthToken):
    """ Custom auth backend"""
    def post(self, request, *args, **kwargs):
        """ get auth token """
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        data = {
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'password': user.password,
            'type':{
                'is_student': user.user_type.is_student,
                'is_admin': user.user_type.is_admin,
                'is_superadmin': user.user_type.is_superadmin,
                }
            }
        if user.user_type.is_student:
            data['is_banned'] = user.student.is_banned
        return Response(data)