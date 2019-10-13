from django.db import models
from polymorphic.models import PolymorphicModel
from questions import QuestionGroup

MAX_NAME = 200


class Paper(PolymorphicModel):
    name = models.CharField(max_length=MAX_NAME)
    questions = models.ManyToManyField(QuestionGroup)
