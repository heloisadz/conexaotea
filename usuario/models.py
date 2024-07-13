from django.db import models
from django.contrib.auth.models import User

class Usuario (User):

    #nome = models.CharField (max_length=100)
    #sobrenome = models.CharField (max_length=150)
    CPF = models.CharField(max_length=11, unique=True, default='-', primary_key=True)
    #idade = models.IntegerField()
    cidade = models.CharField (max_length = 50)
    estado = models.CharField (max_length = 30)
    identificacao = models.CharField (max_length = 50)
    #email = models.CharField (max_length = 200)
    #senha = models.CharField (max_length = 50)

class Profissional(models.Model):
    nome = models.CharField (max_length=100)
    especialidade = models.CharField (max_length=150)
    endereco = models.CharField(max_length=150)
    #cr = models.CharField(max_length=20)
    telefone = models.CharField (max_length = 50)
    descricao = models.CharField (max_length = 200)

