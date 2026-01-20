from django import forms
from .models import Profissional

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'datetime-local'})
        }

        error_messages = {
            'nome': {
                'required': 'O nome do profissional é obrigatório.',
            },
        }