"""QuestionBank view """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from backend.serializers.question_bank_serializer import QuestionBankSerializer
from backend.models.question_bank import QuestionBank
from backend.models.knowledge_node import KnowledgeNode


class QuestionBankList(APIView):
    def get(self, request):
        banks = QuestionBank.objects.all()
        serializer = QuestionBankSerializer(banks, many=True)
        return Response(serializer.data)

    def post(self, request):
        post_data = JSONParser().parse(request)
        post_data.pop("id")

        root = KnowledgeNode.objects.create()
        post_data['root_id'] = root.id
        serializer = QuestionBankSerializer(data=post_data)

        if serializer.is_valid():
            new_bank = serializer.save()
            root.belong_bank = new_bank
            root.save()

            serializer.id = new_bank.id
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class QuestionBankDetial(APIView):
    def get(self, request, pk):
        bank = QuestionBank.objects.get(id=pk)
        serializer = QuestionBankSerializer(bank)
        response = serializer.data
        questions = []
        for i in bank.questiongroup_set.all():
            questions += i
        response['questions'] = questions
        return Response(response)

    def put(self, request, pk):
        bank = QuestionBank.objects.get(id=pk)
        put_data = JSONParser().parse(request)
        serializer = QuestionBankSerializer(bank, put_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
