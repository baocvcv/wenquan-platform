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


class KnowledgeNode(PolymorphicModel):
    """Models for Knowledge Node
    Attributes:
        node_id: identity number of node
        name: name of node
        subnodes: children nodes of node
        questions: children question of node
    """
    node_id = models.CharField()
    name = models.CharField()
    subnodes = models.ManyToManyField("self", symmetrical=False)
    questions = models.ManyToManyField(Question)
