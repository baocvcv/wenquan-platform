""" QuestionRecord View """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions

from backend.models.questions import Question
from backend.models import QuestionRecord
from backend.serializers import QuestionRecordSerializer
from backend.models.questions.question import INT2TYPE
from .users_views import OwnerOnly

class QuestionRecordList(APIView):
    "Create and retrieve question records"
    def get(self, request):
        "Return user record"
        user = request.user
        if user.user_group == "Student" or user.user_group == "Admin":
            # wrong questions only
            question_records = user.questionrecord_set.filter(is_correct=False)
        else:
            question_records = QuestionRecord.objects.all()
        data = QuestionRecordSerializer(question_records, many=True).data
        return Response(data, status.HTTP_200_OK)


    def post(self, request):
        "Create a record"
        data = request.data
        # judge
        question = Question.objects.get(id=data['question_id'])
        if request.user.user_group == 'Student':
            if question.history_version.belong_bank.id not in request.user.question_banks:
                return Response(status.HTTP_403_FORBIDDEN)
        if question.question_type != 5:
            is_correct, _ = question.checker(data['ans'])
        else:
            is_correct = True
        # add record
        record = QuestionRecord(
            user=request.user,
            question_id=data['question_id'],
            question_type=INT2TYPE[str(question.question_type)],
            is_correct=is_correct,
            score=[],
            correct_or_not=[],
        )
        record.set_ans(data['ans'])
        record.save()
        data = QuestionRecordSerializer(record).data
        return Response(data, status=status.HTTP_201_CREATED)

class QuestionRecordDetail(generics.RetrieveAPIView):
    "Retrieve detail info of a record"
    queryset = QuestionRecord.objects.all()
    serializer_class = QuestionRecordSerializer
    permission_classes = [permissions.IsAdminUser | OwnerOnly]
