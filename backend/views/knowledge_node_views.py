""" KnowledgeNode view """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import Http404

from backend.models.knowledge_node import KnowledgeNode


class KnowledgeNodeName(APIView):
    """Get Brief infomation of a KnowledgeNode"""
    def get(self, request, root_id):
        """Only get id and name of node whose id=root_id"""
        try:
            node = KnowledgeNode.objects.get(id=root_id)
        except KnowledgeNode.DoesNotExist:
            raise Http404
        response = {}
        response['id'] = node.id
        response['name'] = node.name
        return Response(response)


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

    def post(self, request):
        """Create a KnowledgeNode"""
        post_data = JSONParser().parse(request)[0]
        self.go_through_tree(1)
        response = post_data
        return Response(response)
