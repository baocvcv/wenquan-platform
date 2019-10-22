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

    def go_through_tree(root_id):
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
        response = go_through_tree(pk)
        return response

    def post(self, request):
        """Create a KnowledgeNode"""
        post_data = JSONParser().parse(request)[0]
        subnodes = []
        parent = KnowledgeNode.get(id=post_data.pop('parent'))

        for i in post_data['subnodes']:
            subnodes += KnowledgeNode.get(id=i)
        post_data['subnodes'] = subnodes
        serializer = KnowlegdeNodeSerializer(post_data)

        if serializer.is_valid:
            new_node = serializer.save()
            parent.subnodes.add(new_node)
            parent.save()
            serializer.id = new_node.id

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
