from django.db import models

class Forum (models.Model):
    id = models.AutoField(primary_key=True, default=None)
    criador = models.CharField (max_length=100)
    data_criação = models.CharField (max_length=20)
    categoria = models.CharField (max_length = 200)
    
# Create your models here.
