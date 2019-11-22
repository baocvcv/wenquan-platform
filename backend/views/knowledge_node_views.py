""" KnowledgeNode view """
from rest_framework.response import Response
from rest_framework import status
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
        child = []
        json['id'] = root_id
        json['name'] = root.name
        child = list(root.subnodes.all())
        while child:
            for i in child:
                child_json.append(self.go_through_tree(i.id))
                child.remove(i)
        json['subnodes'] = child_json
        return json

    def rebuild_tree(self, put_data, root_id):
        """Create new nodes and reconnect or remove old nodes"""
        root = self.get_object(put_data['id'])
        root.name = put_data['name']
        root.subnodes.clear()
        for i in put_data['subnodes']:
            if i['id'] == -1:
                child_node = self.create_node(i['name'], root_id)
                i['id'] = child_node.id
            else:
                child_node = self.get_object(i['id'])
            root.subnodes.add(child_node)
            self.rebuild_tree(i, root_id)
        root.save()

    def create_node(self, name, root_id):
        """Create a KnowledgeNode"""
        parent = self.get_object(root_id)
        bank = parent.question_bank
        new_node = KnowledgeNode.objects.create(name=name)
        new_node.question_bank = bank
        new_node.save()
        return new_node

    def delete_node(self, nodes_id):
        """Remove a knowledge node"""
        for i in nodes_id:
            node = self.get_object(i)
            parent = node.knowledgenode_set.get()
            while parent.id in nodes_id:
                parent = parent.knowledgenode_set.get()
            question = node.questiongroup_set.all()
            for j in question:
                j.parents_node.remove(i)
                j.parents_node.add(parent)

    def get(self, request, root_id):
        """Get a tree whose root's id = root_id"""
        if request.user.user_group == 'Student':
            bank_id = self.get_object(root_id).question_bank.id
            if bank_id not in request.user.question_banks:
                return Response(status=status.HTTP_403_FORBIDDEN)
        response = self.go_through_tree(root_id)
        response['bank_id'] = self.get_object(root_id).question_bank.id
        return Response(response)

    def put(self, request, root_id):
        """Edit tree of node"""
        if request.user.user_group == 'Student':
            return Response(status=status.HTTP_403_FORBIDDEN)
        put_data = JSONParser().parse(request)
        modify = put_data['modify']
        delete = put_data['delete']
        if not root_id == modify['id']:
            return Response({"errors": "root_id != id"}, status=400)
        self.delete_node(delete)
        self.rebuild_tree(modify, root_id)
        response = self.go_through_tree(root_id)
        return Response(response)


class KnowledgeNodeDetail(APIView):
    """View for a KnowledgeNode"""
    @classmethod
    def serializer(cls, node):
        """Create json from KnowledgeNode"""
        questions = []
        for i in node.questiongroup_set.all():
            question = QuestionList.get_latest_version(i)
            questions.append(question.id)

        response = {}
        response['id'] = node.id
        response['name'] = node.name
        response['questions'] = questions
        return response

    def get(self, request, root_id):
        """Get infomation except subnodes"""
        if request.user.user_group == 'Student':
            bank_id = KnowledgeNodeList.get_object(root_id).question_bank.id
            if bank_id not in request.user.question_banks:
                return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            node = KnowledgeNode.objects.get(id=root_id)
        except KnowledgeNode.DoesNotExist:
            raise Http404

        response = self.serializer(node)
        return Response(response)


class NodeQuestionView(APIView):
    """View for question set in nodes"""
    @classmethod
    def go_through_tree(cls, root_id):
        """KnowledgeNode tree level order traversal"""
        root = KnowledgeNodeList.get_object(root_id)
        nodes = []
        child = list(root.subnodes.all())
        for i in child:
            nodes += cls.go_through_tree(i.id)
        nodes.append(root_id)
        return nodes

    def post(self, request):
        """Get question belong to some nodes"""
        response = set()
        post_data = JSONParser().parse(request)
        nodes = post_data['nodes_id']
        temp = []
        for i in nodes:
            if request.user.user_group == 'Student':
                bank_id = KnowledgeNodeList.get_object(i).question_bank.id
                if bank_id not in request.user.question_banks:
                    return Response(status=status.HTTP_403_FORBIDDEN)
            temp += self.go_through_tree(i)

        nodes += temp
        for i in nodes:
            node = KnowledgeNodeList.get_object(i)
            questions = []
            for j in node.questiongroup_set.all():
                question = QuestionList.get_latest_version(j)
                questions.append(question.id)
            response = response | set(questions)
        return Response(list(response))
