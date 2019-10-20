""" KnowledgeNode view """
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from backend.models.knowledge_node import KnowledgeNode


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

        new_node = KnowledgeNode.get(id=serializer.id)
        parent.subnodes.add(new_node)
        parent.save()

        if serializer.is_valid:
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
