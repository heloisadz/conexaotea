from datetime import date
from django.db import models

class Comentario (models.Model):

    idComentario = models.CharField (max_length=100)
    idCriador = models.CharField (max_length=150)
    CPF = models.CharField(max_length=11, unique=True, default='-', primary_key=True)
    data = models.DateField(default=date.today)
   
# Create your models here.
