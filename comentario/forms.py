
from django import forms
from django.utils import timezone
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    corpo = forms.CharField(widget=forms.Textarea, label='Comentário')

    class Meta:
        model = Comentario
        fields = ['corpo']  # Somente 'corpo' é editável pelo usuário

    def save(self, commit=True, user=None):
        comentario = super().save(commit=False)
        if user is not None:
            comentario.user = user
        # Define a data do comentário automaticamente
        
        if commit:
            comentario.save()
        return comentario

