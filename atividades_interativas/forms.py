# usuario/forms.py

from django import forms
from .models import Atividades

class AtividadesForm(forms.ModelForm):

    class Meta:
        model = Atividades
        fields = '__all__'
