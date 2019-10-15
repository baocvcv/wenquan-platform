"""Define the model of Question Banks"""
from django.db import models
from polymorphic.models import PolymorphicModel

from .knowledge_node import KnowledgeNode
from .questions import QuestionGroup

MAX_ID = 20
MAX_NAME = 200


class QuestionBanks(PolymorphicModel):
    """Models for Question Banks
    Attributes:
        node_id: identity number of bank
        name: name of bank
        subnodes: children Knowledg Node of bank
        questions: children question of bank
    """
    node_id = models.CharField(max_length=MAX_ID)
    name = models.CharField(max_length=MAX_NAME)
    subnodes = models.ManyToManyField(KnowledgeNode)
    questions = models.ManyToManyField(QuestionGroup)
