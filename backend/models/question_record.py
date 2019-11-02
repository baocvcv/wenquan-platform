""" Question history records """
from django.db import models
from .questions import BriefAnswerQ
from .questions import SingleChoiceQ
from .questions import MultpChoiceQ
from .questions import FillBlankQ
from .questions import TrueOrFalseQ
from .questions.question import TYPEDIC
from .questions.question import INT2TYPE

class QuestionRecord(models.Model):
    """ Question record entry """
    question_id = models.IntegerField()
    question_type = models.CharField(20)
    record_time = models.DateTimeField(auto_now=True)
    #TODO: same format for question answers???
    ans = models.CharField(max_length=200, default="")
    score = models.IntegerField(blank=True)
    is_correct = models.BooleanField(blank=True)

    def __str__(self):
        " Stringify "
        return "Question %d answered at %s" % (self.question_id, self.record_time)

    def get_question(self):
        "Get the question instance of this record"
        if self.question_type == 'single':
            return SingleChoiceQ.objects.get(id=self.question_id)
        elif self.question_type == 'multiple':
            return MultpChoiceQ.objects.get(id=self.question_id)
        elif self.question_type == 'TorF':
            return TrueOrFalseQ.objects.get(id=self.question_id)
        elif self.question_type == 'fill_blank':
            return FillBlankQ.objects.get(id=self.question_id)
        elif self.question_type == 'brief_ans':
            return BriefAnswerQ.objects.get(id=self.question_id)

    def judge(self):
        "Judge whether the answer is correct and set the score"
        question = self.get_question()
        #TODO: judge not implemented
        result = question.judge(self.ans)
        self.score = result.score
        self.is_correct = result.is_correct
