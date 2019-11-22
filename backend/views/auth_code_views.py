""" Views for auth code """
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from psycopg2 import Error

from backend.models import AuthCode
from backend.models import QuestionBank
from backend.scripts.generate_token import generate_token

class AuthCodeView(APIView):
    """ Handle auth code """

    @staticmethod
    def post(request):
        """ generate auth codes """
        if request.user.user_group == 'Student':
            return Response(status=status.HTTP_403_FORBIDDEN)
        q_bank_id = request.data['question_bank_id']
        q_bank = QuestionBank.objects.get(pk=q_bank_id)
        auth_codes = q_bank.authcode_set.all()
        total_num = len(auth_codes)
        # collect usable codes
        codes = []
        for auth_code in auth_codes:
            if auth_code.is_usable:
                codes.append(auth_code.key)

        if 'num' in request.data:
            # generate new codes
            num = request.data['num']
            for i in range(num):
                key = generate_token()
                code = AuthCode(
                    key=key,
                    question_bank=q_bank
                )
                try:
                    code.save()
                    codes.append(key)
                except Error: # psycopg2 error
                    i -= 1
            total_num += num
        valid_num = len(codes)
        return Response(
            {
                "question_bank_id": q_bank_id,
                "total_num": total_num,
                "valid_num": valid_num,
                "auth_code": codes,
            },
            status.HTTP_200_OK
        )

class AuthCodeDetailView(APIView):
    """ Activate auth code """
    @staticmethod
    def get(request, code):
        " Activate auth code "
        user = request.user
        try:
            auth_code = AuthCode.objects.get(key=code)
        except ObjectDoesNotExist:
            return Response({'error': 'Code is invalid'}, status.HTTP_400_BAD_REQUEST)
        if auth_code.is_usable:
            auth_code.is_usable = False
            auth_code.save()
            user.question_banks.append(auth_code.question_bank.id)
            user.save()
            return Response({}, status.HTTP_200_OK)
        return Response({'error': 'Code is invalid'}, status.HTTP_400_BAD_REQUEST)
