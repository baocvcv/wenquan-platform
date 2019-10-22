"""Define the model of Knowledge Node"""
from django.db import models
from polymorphic.models import PolymorphicModel
from .question_bank import QuestionBank

MAX_ID = 20
MAX_NAME = 200


class KnowledgeNode(PolymorphicModel):
    """Models for Knowledge Node
    Attributes:
        node_id: identity number of node
        name: name of node
        subnodes: children nodes of node
        questions: children question of node
    """
    question_bank = models.ForeignKey(QuestionBank, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=MAX_NAME)
    subnodes = models.ManyToManyField("self", symmetrical=False)
