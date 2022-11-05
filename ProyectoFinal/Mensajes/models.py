from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=100)
