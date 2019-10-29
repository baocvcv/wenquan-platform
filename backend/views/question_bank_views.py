"""QuestionBank view """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import Http404

from backend.serializers.question_bank_serializer import QuestionBankSerializer
from backend.models.question_bank import QuestionBank
from backend.models.knowledge_node import KnowledgeNode
from .question_views import QuestionList


class QuestionBankList(APIView):
    """View of all QuestionBank"""
    def get(self, request):
        """Get list of all QuestionBank"""
        banks = QuestionBank.objects.all()
        response = []
        for i in banks:
            response.append(i.id)
        return Response(response)

    def post(self, request):
        """Create a new QuestionBank"""
        post_data = JSONParser().parse(request)
        if "id" in post_data:
            post_data.pop("id")
        root = KnowledgeNode.objects.create()
        post_data['root_id'] = root.id
        serializer = QuestionBankSerializer(data=post_data)
        if serializer.is_valid():
            new_bank = serializer.save()
            root.question_bank = new_bank
            root.save()
            response = serializer.data
            response['id'] = new_bank.id
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
        bank = self.get_object(bank_id)
        put_data = JSONParser().parse(request)
        serializer = QuestionBankSerializer(bank, put_data)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            response['id'] = bank.id
            return Response(response, status=200)
        return Response(serializer.errors, status=400)
