from django import forms
from .models import Ativo

class AtivoForm(forms.ModelForm):
    class Meta:
        model = Ativo
        fields = ['nome', 'codigo', 'limite_inferior', 'limite_superior', 'periodicidade']