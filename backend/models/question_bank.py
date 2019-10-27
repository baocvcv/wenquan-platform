"""Define the model of Question Banks"""
from django.db import models
from polymorphic.models import PolymorphicModel

MAX_CONTENT = 20000
MAX_ID = 20
MAX_NAME = 200
MAX_URL = 10000000


class QuestionBank(PolymorphicModel):
    """Models for Question Banks
    Attributes:
        root_id: The id of root KnowledgeNode
        name: Name of bank
        picture: The url of banks icon
        brief: The brief introduction of bank
        createTime: The date and time when bank was created
        lastUpdate: The date and time of the latest modifying
        authority: The authority of bank
        question_count: The number of QuestionGroup related to bank
        invitation_code_count: The number of invitation code of bank
        activated_code_count: The number of activated invitation bank
    """
    root_id = models.IntegerField()
    name = models.CharField(max_length=MAX_NAME)
    picture = models.CharField(max_length=MAX_URL)
    brief = models.CharField(max_length=MAX_CONTENT)
    createTime = models.DateTimeField()
    lastUpdate = models.DateTimeField()
    authority = models.CharField(max_length=MAX_NAME)
    question_count = models.IntegerField()
    invitation_code_count = models.IntegerField()
    activated_code_count = models.IntegerField()
