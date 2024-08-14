from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    mail = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User , on_delete=models.CASCADE)
