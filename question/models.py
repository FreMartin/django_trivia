from django.contrib.auth.models import User
from django.db import models

from level.models import Level

class Question(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    text = models.TextField()
    correct_answer = models.CharField(max_length=255)
    incorrect_answers = models.JSONField()  # Almacenar las respuestas incorrectas, puede ser en un array JSON 

    def __str__(self):
        return self.text
