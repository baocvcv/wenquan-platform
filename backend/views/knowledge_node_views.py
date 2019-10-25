""" KnowledgeNode view """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from backend.serializers.knowledge_node_serializer import KnowlegdeNodeSerializer
from backend.models.knowledge_node import KnowledgeNode


class KnowledgeNodeName(APIView):
    """Only get nodes' names and ids"""
    def get(self, request, pk):
        node = KnowledgeNode.objects.get('id=pk')
        response = {}
        response['id'] = node.id
        response['name'] = node.name
        return Response(response)


class KnowledgeNodeList(APIView):
    """Get all Node info or create a question"""
    tree = []

    def go_through_tree(self, root_id):
        root = KnowledgeNode.objects.get(id=root_id)
        json = {}
        child_json = []
        json['id'] = root_id
        child = root.subnodes.all()
        while len(child) != 0:
            for i in child:
                child_json += go_through_tree(child.id)
        json['subnodes'] = child_json
        return json

    def get(self, request, pk):
        response = self.go_through_tree(pk)
        response['bank_id'] = KnowledgeNode.objects.get(id=pk).question_bank.id
        return Response(response)

    def post(self, request, pk):
        """Create a KnowledgeNode"""
        post_data = JSONParser().parse(request)[0]
