"""Define model of subjects"""

from django.db import models
from polymorphic.models import PolymorphicModel
from question_banks import QuestionBanks


class subjects(PolymorphicModel):
    """Model for Subjects
    Attributs:
        name: name of subjects
        question_banks: child question banks of subjects
    """
    name = models.CharField(max_length=30)
    question_banks = models.ManyToManyField(QuestionBanks)
