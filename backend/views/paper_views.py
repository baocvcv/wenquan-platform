"""Paper view """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import Http404

from backend.models.paper import Paper
from backend.models.paper import Section
from backend.serializers.paper_serializer import PaperSerializer
from backend.serializers.paper_serializer import SectionSerializer
from .question_views import QuestionDetail


class PaperList(APIView):
    """View of all QuestionBank"""
    @classmethod
    def create_sections_from_data(cls, data):
        """Create Section objects from json"""
        section_objects = []
        for i in data:
            if "id" in i:
                i.pop("id")
            question_list = i.pop("questions", [])
            new_section = Section.objects.create(**i)
            for j in question_list:
                target = QuestionDetail.get_object(j['id'])
                point_every_blank = []
                if "point_every_blank" in j:
                    point_every_blank = j['point_every_blank']
                new_section.questions.add(
                    target,
                    through_defaults={
                        "question_point": j['question_point'],
                        "question_num": j["question_num"],
                        "point_every_blank": point_every_blank
                    },
                )
                section_objects.append(new_section)
        return section_objects

    @classmethod
    def create_paper_from_data(cls, data):
        """Create Paper objects from json"""
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
        """Create json from Paper objects"""
        serializer = PaperSerializer(paper)
        response = serializer.data
        response['sections'] = []
        for i in paper.section_set.all():
            section_data = {}
            section_data['id'] = i.id
            section_data['section_num'] = i.section_num
            response['sections'].append(section_data)
        response['sections'].sort(key=lambda x: x['section_num'])
        return response

    def get(self, request):
        """Get a list of all Paper"""
        papers = Paper.objects.all()
        response = []
        for i in papers:
            if not i.is_latest:
                continue
            paper_data = self.create_response_from_paper(i)
            response.append(paper_data)
        return Response(response)

    def post(self, request):
        """Create a Paper"""
        post_data = JSONParser().parse(request)
        new_paper = self.create_paper_from_data(post_data)
        response = self.create_response_from_paper(new_paper)
        return Response(response)


class SectionDetail(APIView):
    """View for details of Section"""
    @classmethod
    def get_object(cls, section_id):
        """Get Section objects whose id=section_id"""
        try:
            return Section.objects.get(id=section_id)
        except Section.DoesNotExist:
            raise Http404

    def get(self, request, section_id):
        """Get details of Section whose id=section_id"""
        section = self.get_object(section_id)
        serializer = SectionSerializer(section)
        response = serializer.data
        questions = []
        for i in section.questions.all():
            question_data = {}
            q_on_paper = i.questionversion_set.get(section=section)
            question_data['id'] = i.id
            question_data['question_point'] = q_on_paper.question_point
            question_data['question_num'] = q_on_paper.question_num
            question_data['point_every_blank'] = q_on_paper.point_every_blank
            questions.append(question_data)
        questions.sort(key=lambda x: x['question_num'])
        response['questions'] = questions
        return Response(response)


class PaperDetail(APIView):
    """View for Paper details"""
    @classmethod
    def get_object(cls, paper_id):
        """Get Paper objects whose id=paper_id"""
        try:
            return Paper.objects.get(id=paper_id)
        except Paper.DoesNotExist:
            raise Http404

    def get(self, request, paper_id):
        """Get details of Paper whose id=paper_id"""
        paper = self.get_object(paper_id)
        response = PaperList.create_response_from_paper(paper)
        return Response(response)

    def put(self, request, paper_id):
        """Modify Paper whose id=paper_id"""
        paper = self.get_object(paper_id)
        put_data = JSONParser().parse(request)
        if "change_status" in put_data:
            new_status = put_data["change_status"]
            if not new_status == "public" and not new_status == "drafted":
                return Response("Error: status should be \"public\" or \"drafted\"")
            paper.status = new_status
            paper.save()
            return Response(PaperList.create_response_from_paper(paper))
        paper.is_latest = False
        paper.save()
        new_paper = PaperList.create_paper_from_data(put_data)
        response = PaperList.create_response_from_paper(new_paper)
        return Response(response)
