# forum/forms.py

from django import forms
from django.contrib.auth.models import User  # Importe o modelo User
from .models import Forum
from django.utils import timezone

class ForumForm(forms.ModelForm):
    CATEGORIA_CHOICES = [
        ('opcao1', 'Opção 1'),
        ('opcao2', 'Opção 2'),
        ('opcao3', 'Opção 3'),
    ]
    categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES)
    corpo = forms.CharField(widget=forms.Textarea)
    datacriacao = forms.DateField(widget=forms.HiddenInput(), initial=timezone.now().date())
   
    class Meta:
        model = Forum
        fields = ('categoria', 'corpo', 'datacriacao')  # Defina os campos que o usuário precisa preencher
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Pegue o usuário dos argumentos
        super().__init__(*args, **kwargs)
        # Esconda o campo user e defina-o automaticamente
        self.fields['user'] = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput(), required=False)
    
    def save(self, commit=True):
        forum = super().save(commit=False)
        if self.user:
            forum.user = self.user  # Defina o usuário no objeto forum
        forum.datacriacao = timezone.now().date()
        if commit:
            forum.save()
        return forum
