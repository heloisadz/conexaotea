from django.db import models

class Biblioteca(models.Model):
    complexidade = models.CharField (max_length=7)
    titulo = models.CharField (max_length=100)
    categoria = models.CharField(max_length=7)