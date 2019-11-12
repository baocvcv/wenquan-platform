""" Paper history records """
from django.db import models
from .questions import BriefAnswerQ
from .questions import SingleChoiceQ
from .questions import MultpChoiceQ
from .questions import FillBlankQ
from .questions import TrueOrFalseQ
from .paper import Paper
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

class PaperRecord(models.Model):
    """ Question record entry """
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    record_time = models.DateTimeField(auto_now=True)
    # time fields
    is_timed = models.BooleanField(default=False)
    start_time = models.DateTimeField(auto_now=True)
    time_left = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    # point fields
    user_total_points = models.IntegerField(default=0)
    user_section_points = ArrayField(models.IntegerField(), default=list)

    def update_time(self):
        if not self.is_active:
            return
        time_delta = timezone.now().fromtimestamp(self.start_time)
        self.time_left -= time_delta
        if self.time_left <= 0:
            self.is_active = False

    def can_update(self):
        return self.is_active and self.time_left > 0

    def judge(self):
        " Calculate section and whole paper points "
        pass
