""" PaperRecord View """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
# from django.utils import timezone
# from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from backend.models import QuestionRecord
from backend.models import PaperRecord
# from backend.models import Paper
from backend.models.questions import Question
from backend.models.questions.question import INT2TYPE
from backend.serializers import QuestionRecordSerializer
from backend.serializers import PaperRecordSerializer

class PaperRecordList(generics.ListAPIView):
    "Create and retrieve paper record"
    queryset = PaperRecord.objects.all()
    serializer_class = PaperRecordSerializer

class PaperRecordDetail(APIView):
    "Update and retrieve paper record"

    @staticmethod
    def get(request, record_id):
        "Get the detail of a paper record"
        paper_record = PaperRecord.objects.get(id=record_id)
        paper_record_data = PaperRecordSerializer(paper_record).data
        # compile questions
        question_data = {}
        paper = paper_record.paper
        for question in paper.question_record_set.all():
            q_data = QuestionRecordSerializer(question)
            question_data[str(q_data.question_id)] = q_data
        paper_record_data['questions'] = question_data
        return Response(paper_record_data, status.HTTP_200_OK)

    @staticmethod
    def post(request, record_id):
        " Update paper record "
        paper_record = PaperRecord.objects.get(id=record_id)
        # error
        if not paper_record.can_update():
            return Response(
                {"error": "Paper no longer active."},
                status=status.HTTP_400_BAD_REQUEST,
                )
        # paper = Paper.objects.get(id=request.data['paper_id'])
        # sections = paper.section_set.all()
        section_datas = request.data['sections']
        for section_data in section_datas:
            question_datas = section_data['questions']
            for q_data in question_datas:
                question = Question.objects.get(id=q_data['id'])
                is_correct, scores = question.checker(
                    q_data['ans'],
                    section_data['id']
                )
                try:
                    question_record = paper_record.question_record_set.get(
                        question_id=q_data['id'],
                    )
                except ObjectDoesNotExist:
                    question_record = QuestionRecord(
                        question_id=q_data['id'],
                        question_type=INT2TYPE[question.question_type],
                        is_correct=is_correct,
                        score=scores,
                        paper_record=paper_record
                    )
                question_record.set_ans(q_data['ans'])
                question_record.save()

        # update status of paper record
        if 'action' in request.data:
            cmd = request.data['action']
            if cmd == 'pause':
                paper_record.is_active = False
            elif cmd == 'continue':
                paper_record.is_active = True
            elif cmd == 'finish':
                paper_record.is_active = False
                paper_record.time_left = 0
        paper_record.save()

        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def put(request, record_id):
        "Modify a question record"
        paper_record = PaperRecord.objects.get(id=record_id)
        q_id = request.data['question_id']
        question_record = paper_record.question_record_set.get(
            question_id=q_id
        )
        score = request.data['score']
        if isinstance(score, int):
            if question_record.question_type == "fill_blank":
                question = Question.objects.get(id=q_id)
                question_record.score = [score] * question.question_blank_num
            else:
                question_record.score = [score]
        else:
            question_record.score = score
        question_record.save()

        return Response(status=status.HTTP_200_OK)
