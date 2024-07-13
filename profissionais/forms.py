# usuario/forms.py

from django import forms
from .models import Profissional

class ProfissionalForm(forms.ModelForm):

    class Meta:
        model = Profissional
        fields = ['nome', 'especialidade', 'endereco', 'telefone', 'descricao']
