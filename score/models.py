from django.contrib.auth.models import User
from django.db import models

from level.models import Level

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_time = models.DurationField()

    def __str__(self):
        return f"{self.user.username} - {self.level.name} - {self.score}"
