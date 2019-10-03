"""Define the model of Knowledge Node"""
from django.db import models
from polymorphic.models import PolymorphicModel

from questions.question import Question
from questions.brief_answer_q import BriefAnswerQ
from questions.choice_question import SingleChoiceQ, MultpChoiceQ
from questions.fill_blank_q import FillBlankQ


class KnowledgeNode(PolymorphicModel):
    node_id = models.CharField()
    name = models.CharField()
    subnodes = models.ManyToManyField(KnowledgeNode)
    questions = models.ManyToManyField(Question)
