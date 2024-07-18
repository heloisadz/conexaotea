from django.db import models
from django.contrib.auth.models import User

class Forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datacriacao = models.DateField()
    categoria = models.CharField(max_length=150)
    corpo = models.CharField(max_length=2000)
