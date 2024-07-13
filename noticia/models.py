from django.db import models

class Noticia (models.Model):
    idNoticia = models.AutoField(primary_key=True, default=None)
    titulo = models.CharField (max_length=100)
    data_publi = models.CharField (max_length=20)
    referencias = models.CharField (max_length = 200)
    
# Create your models here.
