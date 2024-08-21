from django.db import models

class Atividades(models.Model):
    nome = models.CharField (max_length=100)
    tipo = models.CharField (max_length=100)
    descricao = models.CharField(max_length=500)