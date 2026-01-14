from django import forms       
from .models import Paciente

#Criando formulario

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nome completo',
            'data_nascimento',
            'diagnostico_principal',
            'familiar_responsavel',
            'contato_familiar',
            'observacoes',
        ]