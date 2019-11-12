""" Views for auth code """
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from backend.models import AuthCode
from backend.serializers import AuthCodeSerializer
from backend.models import QuestionBank
from backend.scripts.email_verification import generate_token

class AuthCodeView(APIView):
    """ Handle auth code """

    @staticmethod
    def post(request):
        """ generate auth codes """
        q_bank_id = request.data['question_bank_id']
        q_bank = QuestionBank.objects.get(pk=q_bank_id)
        auth_codes = q_bank.auth_code_set.all()
        total_num = len(auth_codes)
        # collect usable codes
        codes = []
        for auth_code in auth_codes:
            if auth_code.is_usable:
                codes.append(auth_code.key)

        if 'num' in request.data:
            # generate new codes
            #TODO: problem! codes may duplicate and cause errors
            num = request.data['num']
            for _i in range(num):
                key = generate_token()
                code = AuthCode(
                    key=key,
                    question_bank=q_bank
                )
                code.save()
                codes.append(key)
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
            return Response(status.HTTP_200_OK)
        return Response({'error': 'Code is invalid'}, status.HTTP_400_BAD_REQUEST)
