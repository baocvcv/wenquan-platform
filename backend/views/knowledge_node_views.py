""" KnowledgeNode view """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import Http404

from backend.models.knowledge_node import KnowledgeNode
from .question_views import QuestionList


class KnowledgeNodeList(APIView):
    """View for all KnowledgeNode"""
    tree = []

    @classmethod
    def get_object(cls, root_id):
        """Get the KnowledgeNode with id=root_id"""
        try:
            return KnowledgeNode.objects.get(id=root_id)
        except KnowledgeNode.DoesNotExist:
            raise Http404

    def go_through_tree(self, root_id):
        """KnowledgeNode tree level order traversal"""
        root = self.get_object(root_id)
        json = {}
        child_json = []
        json['id'] = root.id
        json['name'] = root.name
        child = root.subnodes.all()
        while child:
            for i in child:
                child_json += self.go_through_tree(i.id)
        json['subnodes'] = child_json
        return json

    def get(self, request, root_id):
        """Get a tree whose root's id = root_id"""
        response = self.go_through_tree(root_id)
        response['bank_id'] = self.get_object(root_id).question_bank.id
        return Response(response)

    def post(self, request, root_id):
        """Create a KnowledgeNode"""
        post_data = JSONParser().parse(request)[0]
        parent = self.get_object(post_data['parent'])
        bank = parent.question_bank
        new_node = KnowledgeNode.objects.create(name=post_data['name'])
        new_node.question_bank = bank
        new_node.save()
        parent.subnodes.add(new_node)
        response = {}
        response['id'] = new_node.id
        response['name'] = new_node.name
        response['parent'] = parent.id
        response['subnodes'] = []
        return Response(response)


class KnowledgeNodeName(APIView):
    """View for a KnowledgeNode"""
    @classmethod
    def serializer(cls, node):
        """Create json from KnowledgeNode"""
        questions = []
        for i in node.questiongroup_set.all():
            question = QuestionList.get_latest_version(i)
            questions.append(question.id)

        response = {}
        response['id'] = nood.id
        response['name'] = node.name
        response['questions'] = questions
        return response

    def get(self, request, root_id):
        """Get infomation except subnodes"""
        try:
            node = KnowledgeNode.objects.get(id=root_id)
        except KnowledgeNode.DoesNotExist:
            raise Http404

        response = self.serializer(node)
        return Response(response)

    def put(self, request, root_id):
        """Modify infomation"""
        put_data = JSONParser().parse(request)[0]
        node = self.KnowledgeNodeList.get_object(root_id)
        node.name = put_data['name']
        node.save()
        response = self.serializer(node)
        return Response(response)
