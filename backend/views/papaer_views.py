"""Paper view """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import Http404

from backend.models.paper import Paper
from backend.models.paper import Section
from backend.serializers.paper_serializer import PaperSerializer
from .question_views import QuestionDetail


class PaperList(APIView):
    """View of all QuestionBank"""
    @classmethod
    def create_sections_from_data(cls, data):
        section_objects = []
        for i in data:
            '''--TODO: input examine--'''
            question_list = i.pop("questions", [])
            new_section = Section.objects.create(**i)
            for j in question_list:
                target = QuestionDetail.get_object(j['id'])
                new_section.questions.add(
                    target,
                    through_defaults={
                        "question_point": j['question_point'],
                    },
                )
                section_objects.append(new_section)
        return section_objects

    @classmethod
    def create_paper_from_data(cls, data):
        if "id" in data:
            data.pop("id")
        if "sections" not in data:
            return Response({"errors": "sections is required"}, status=400)
        sections = data.pop("sections")
        section_objects = cls.create_sections_from_data(sections)
        new_paper = Paper.objects.create(**data)
        new_paper.save()
        for i in section_objects:
            i.belong_paper = new_paper
            i.save()
        return new_paper

    @classmethod
    def create_response_from_paper(cls, paper):
        serializer = PaperSerializer(paper)
        response = serializer.data
        response['sections'] = []
        for i in paper.section_set.all():
            response['sections'].append(i.id)
        return response

    def get(self, request):
        papers = Paper.objects.all()
        response = []
        for i in papers:
            if not i.is_latest:
                continue
            paper_data = self.create_response_from_paper(i)
            response.append(paper_data)
        return Response(response)

    def post(self, request):
        post_data = JSONParser().parse(request)
        new_paper = self.create_paper_from_data(post_data)
        response = self.create_response_from_paper(new_paper)
        return Response(response)


class PaperDetail(APIView):
    @classmethod
    def get_object(cls, paper_id):
        try:
            return Paper.objects.get(id=paper_id)
        except Paper.DoesNotExist:
            raise Http404

    def get(self, request, paper_id):
        paper = self.get_object(paper_id)
        response = PaperList.create_response_from_paper(paper)
        return Response(response)

    def put(self, request, paper_id):
        paper = self.get_object(paper_id)
        paper.is_latest = False
        put_data = JSONParser().parse(request)
        new_paper = PaperList.create_paper_from_data(put_data)
        response = PaperList.create_response_from_paper(new_paper)
        return Response(response)
