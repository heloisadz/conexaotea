from django.db import models
from django.contrib.auth.models import User
from forum.models import Forum

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datacomentario = models.DateTimeField(auto_now_add=True)
    corpo = models.CharField(max_length=2000)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)  # Renomeado de id_forum para forum
