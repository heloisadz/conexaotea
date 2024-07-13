from django import forms
from .models import atividades_interativas

class atividadesForm(forms.ModelForm):

    class Meta:
        model = atividades_interativas
        fields = '__all__'