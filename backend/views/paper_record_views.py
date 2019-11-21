""" PaperRecord View """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from backend.models import QuestionRecord
from backend.models import PaperRecord
from backend.models import Paper
from backend.models.questions import Question
from backend.models.questions.question import INT2TYPE
from backend.serializers import QuestionRecordSerializer
from backend.serializers import PaperRecordSerializer

class PaperRecordList(APIView):
    "Create and retrieve paper record"
    @staticmethod
    def get(request):
        "retrieve records"
        user = request.user
        if user.user_group == 'Student':
            if 'paper' in request.GET:
                paper_records = user.paperrecord_set.filter(paper__id=request.GET['paper'])
            else:
                paper_records = user.paperrecord_set.all()
        else:
            if 'paper' in request.GET:
                paper_records = PaperRecord.objects.filter(paper__id=request.GET['paper'])
            else:
                paper_records = PaperRecord.objects.all()
        return Response(
            PaperRecordSerializer(paper_records, many=True).data,
            status.HTTP_200_OK
        )

    @staticmethod
    def post(request):
        " create record "
        paper = Paper.objects.get(pk=request.data['paper_id'])
        paper_record = PaperRecord(
            user=request.user,
            paper=paper,
            is_timed=request.data['is_timed'],
            time_left=paper.time_limit,
            need_judging=paper.have_brief_ans,
        )
        paper_record.save()
        return Response(
            PaperRecordSerializer(paper_record).data,
            status.HTTP_201_CREATED
        )

class PaperRecordDetail(APIView):
    "Update and retrieve paper record"

    @staticmethod
    def get(request, record_id):
        "Get the detail of a paper record"
        paper_record = PaperRecord.objects.get(id=record_id)
        if request.user.user_group == 'Student' and paper_record.user != request.user:
            return Response(status.HTTP_403_FORBIDDEN)
        paper_record_data = PaperRecordSerializer(paper_record).data
        # compile questions
        question_data = {}
        for question in paper_record.questionrecord_set.all():
            q_data = QuestionRecordSerializer(question).data
            question_data[question.question_id] = q_data
        paper_record_data['questions'] = question_data
        return Response(paper_record_data, status.HTTP_200_OK)


    @staticmethod
    def post(request, record_id):
        " Update paper record "
        paper_record = PaperRecord.objects.get(id=record_id)
        if request.user.user_group == 'Student' and paper_record.user != request.user:
            return Response(status.HTTP_403_FORBIDDEN)
        if not paper_record.can_update():
            return Response(
                {"error": "Paper no longer active."},
                status=status.HTTP_400_BAD_REQUEST,
                )
        if 'sections' in request.data:
            section_datas = request.data['sections']
        else:
            section_datas = []
        for section_data in section_datas:
            question_datas = section_data['questions']
            for q_data in question_datas:
                question = Question.objects.get(id=q_data['id'])
                if question.question_type != 5:
                    is_correct, scores = question.checker(
                        q_data['ans'],
                        section_data['id']
                    )
                else:
                    is_correct = True
                    scores = []
                try:
                    question_record = paper_record.questionrecord_set.get(
                        question_id=q_data['id'],
                    )
                    question_record.score = scores
                except ObjectDoesNotExist:
                    question_record = QuestionRecord(
                        question_id=q_data['id'],
                        question_type=INT2TYPE[str(question.question_type)],
                        is_correct=is_correct,
                        score=scores,
                        paper_record=paper_record,
                        correct_or_not=[],
                        user=request.user,
                    )
                question_record.set_ans(q_data['ans'])
                question_record.save()

        PaperRecordDetail.update_status(request, paper_record)
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def update_status(request, paper_record):
        "update status of paper record"
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

    @staticmethod
    def put(request, record_id):
        "Modify a question record"
        if request.user.user_group == 'Student':
            return Response(status.HTTP_403_FORBIDDEN)
        paper_record = PaperRecord.objects.get(id=record_id)
        if 'action' in request.data:
            paper_record.need_judging = False
            paper_record.save()

        if 'question_id' in request.data:
            q_id = request.data['question_id']
            question_record = paper_record.questionrecord_set.get(
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
            if 'comment' in request.data:
                question_record.comment = request.data['comment']
            if 'correct_or_not' in request.data:
                question_record.correct_or_not = request.data['correct_or_not']
            question_record.save()

        return Response(status=status.HTTP_200_OK)
