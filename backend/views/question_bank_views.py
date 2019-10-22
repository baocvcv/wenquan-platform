"""QuestionBank view """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from backend.serializers.question_bank_serializer import QuestionBankSerializer
from backend.models.question_bank import QuestionBank


class QuestionBankList(APIView):
    def get(self, request):
        banks = QuestionBank.objects.all()
        serializer = QuestionBankSerializer(banks, many=True)
        return Response(serializer.data)

    def post(self, request):
        post_data = JSONParser().parse(request)[0]
        post_data.pop('id')

        root = KnowledgeNode.objects.create()
        post_data['root_id'] = root.id
        serializer = QuestionBankSerializer(**post_data)

        if question_bank.is_valid():
            new_bank = serializer.save()
            root.belong_bank = new_bank
            root.save()

            serializer.id = new_bank.id
            return Response(serializer.data, status=200)
        return Response(serializer.error, status=400)
