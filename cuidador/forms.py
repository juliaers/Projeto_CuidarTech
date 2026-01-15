from django import forms
from .models import Cuidador

class SetorForm(forms.ModelForm):
    class Meta:
        model = Cuidador
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'datetime-local'})
        }

        error_messages = {
            'nome': {
                'required': 'O nome do profissional é obrigatório.',
            },
        }