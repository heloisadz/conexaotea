from django.db import models

class Biblioteca (models.Model):

    categoria = models.CharField (max_length=150)
    
    complexidade = models.CharField (max_length = 200)
    
# Create your models here.
