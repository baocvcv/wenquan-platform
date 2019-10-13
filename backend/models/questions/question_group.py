from django.db import models
from polymorphic.models import PolymorphicModel


class QuestionGroup(PolymorphicModel):
    group_id = models.IntegerField()
    current_version = models.DateTimeField()
