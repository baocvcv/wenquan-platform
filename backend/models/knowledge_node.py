"""Define the model of Knowledge Node"""
from django.db import models
from polymorphic.models import PolymorphicModel

from questions.question import Question
from questions.brief_answer_q import BriefAnswerQ
from questions.choice_question import SingleChoiceQ, MultpChoiceQ
from questions.fill_blank_q import FillBlankQ

BriefAnswerQ()
SingleChoiceQ()
MultpChoiceQ()
FillBlankQ()

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
    name = models.CharField(max_length=MAX_NAME)
    subnodes = models.ManyToManyField("self", symmetrical=False)
    questions = models.ManyToManyField(Question)
