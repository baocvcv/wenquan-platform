"""Define the model of Knowledge Node"""
from django.db import models
from polymorphic.models import PolymorphicModel
from .question_bank import QuestionBanks

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
    node_id = models.CharField(max_length=MAX_ID)
    question_bank = models.ForeignKey(QuestionBanks)
    name = models.CharField(max_length=MAX_NAME)
    subnodes = models.ManyToManyField("self", symmetrical=False)
