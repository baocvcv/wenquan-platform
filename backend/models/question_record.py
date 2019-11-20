""" Question history records """
from django.db import models
from django.contrib.postgres.fields import ArrayField
from .questions import BriefAnswerQ
from .questions import SingleChoiceQ
from .questions import MultpChoiceQ
from .questions import FillBlankQ
from .questions import TrueOrFalseQ

from .paper_record import PaperRecord
from .user import User

class QuestionRecord(models.Model):
    """ Question record entry """
    # basic info
    question_id = models.IntegerField()
    question_type = models.CharField(max_length=20, default="")
    record_time = models.DateTimeField(auto_now=True)
    # answer and scores
    ans = ArrayField(models.CharField(max_length=20000, default=""))
    score = ArrayField(models.IntegerField())
    is_correct = models.BooleanField(blank=True)
    # key to paper record
    paper_record = models.ForeignKey(PaperRecord, on_delete=models.CASCADE, null=True)
    # user
    #!!!!!!!!!!to do: remove blank true
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # for judging
    correct_or_not = ArrayField(models.BooleanField())
    comment = models.CharField(max_length=500, default="")

    def __str__(self):
        " Stringify "
        return "Question %d answered at %s" % (self.question_id, self.record_time)

    def get_question(self):
        "Get the question instance of this record"
        if self.question_type == 'single':
            return SingleChoiceQ.objects.get(id=self.question_id)
        if self.question_type == 'multiple':
            return MultpChoiceQ.objects.get(id=self.question_id)
        if self.question_type == 'TorF':
            return TrueOrFalseQ.objects.get(id=self.question_id)
        if self.question_type == 'fill_blank':
            return FillBlankQ.objects.get(id=self.question_id)
        if self.question_type == 'brief_ans':
            return BriefAnswerQ.objects.get(id=self.question_id)
        return None

    def set_ans(self, ans):
        "Set the answer to the question"
        if ans == "":
            self.ans = []
        else:
            if self.question_type == 'single':
                self.ans = [ans]
            elif self.question_type == 'multiple':
                self.ans = ans
            elif self.question_type == 'TorF':
                if ans:
                    self.ans = ["true"]
                else:
                    self.ans = ["false"]
            elif self.question_type == 'fill_blank':
                self.ans = ans
            elif self.question_type == 'brief_ans':
                self.ans = [ans]
