from django.db import models

class atividades_interativas (models.Model):

    tipo_indicacao = models.CharField (max_length = 200)
