from django.db import models

class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publi = models.DateTimeField(max_length=8)
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    referencia = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
