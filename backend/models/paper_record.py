""" Paper history records """
from django.db import models
from .questions import BriefAnswerQ
from .questions import SingleChoiceQ
from .questions import MultpChoiceQ
from .questions import FillBlankQ
from .questions import TrueOrFalseQ

class PaperRecord(models.Model):
    """ Question record entry """
    pass