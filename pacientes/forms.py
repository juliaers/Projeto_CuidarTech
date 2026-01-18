from django import forms       
from .models import Paciente

#Criando formulario

from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nome_completo': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'diagnostico_principal': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'familiar_responsavel': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'contato_familiar': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
