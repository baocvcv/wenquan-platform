"""QuestionBank view """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import Http404
from psycopg2 import Error

from backend.serializers.question_bank_serializer import QuestionBankSerializer
from backend.models.question_bank import QuestionBank
from backend.models.knowledge_node import KnowledgeNode
from backend.models.auth_code import AuthCode
from backend.scripts.generate_token import generate_token
from .question_views import QuestionList


class QuestionBankList(APIView):
    """View of all QuestionBank"""
    @classmethod
    def create_auth_code(cls, bank):
        """Init authority code"""
        num = bank.invitation_code_count
        for j in range(num):
            key = generate_token()
            code = AuthCode(key=key, question_bank=bank)
            try:
                code.save()
            except Error:
                j -= 1

    def get(self, request):
        """Get list of all QuestionBank"""
        banks = QuestionBank.objects.all()
        response = []
        for i in banks:
            response.append(i.id)
        return Response(response)

    def post(self, request):
        """Create a new QuestionBank"""
        if request.user.user_group != 'Admin' or request.user.user_group != 'SuperAmdin':
            return Response(status=status.HTTP_403_FORBIDDEN)
        post_data = JSONParser().parse(request)
        if "id" in post_data:
            post_data.pop("id")
        root = KnowledgeNode.objects.create()
        root.name = "Root"
        post_data['root_id'] = root.id
        serializer = QuestionBankSerializer(data=post_data)
        if serializer.is_valid():
            new_bank = serializer.save()
            root.question_bank = new_bank
            root.save()
            response = serializer.data
            response['id'] = new_bank.id
            self.create_auth_code(new_bank)
            return Response(response, status=200)
        return Response(serializer.errors, status=400)


class QuestionBankDetail(APIView):
    """View for a QuestionBank"""
    @classmethod
    def get_object(cls, bank_id):
        """Get QuestionBank with id=bank_id"""
        try:
            return QuestionBank.objects.get(id=bank_id)
        except QuestionBank.DoesNotExist:
            raise Http404

    def get(self, request, bank_id):
        """Get infomation of QuestionBank whose id=root_id"""
        bank = self.get_object(bank_id)
        serializer = QuestionBankSerializer(bank)
        response = serializer.data
        questions = []

        for i in bank.questiongroup_set.all():
            if not i.question_set.all():
                continue
            question = QuestionList.get_latest_version(i)
            questions.append(question.id)

        response['questions'] = questions
        response['id'] = bank.id
        return Response(response)

    def put(self, request, bank_id):
        """Update the infomation of QuestionBank whose id=root_id"""
        if request.user.user_group != 'Admin' or request.user.user_group != 'SuperAmdin':
            return Response(status=status.HTTP_403_FORBIDDEN)
        bank = self.get_object(bank_id)
        put_data = JSONParser().parse(request)
        serializer = QuestionBankSerializer(bank, put_data)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            response['id'] = bank.id
            return Response(response, status=200)
        return Response(serializer.errors, status=400)
