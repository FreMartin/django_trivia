from django.contrib.auth.models import User
from django.db import models

from answer.models import Answer
from question.models import Question

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    response_time = models.DurationField()

    def __str__(self):
        return f"{self.user.username} - {self.question.text} - {self.selected_answer.text}"

