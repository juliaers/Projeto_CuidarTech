from django import forms
from .models import Profissional

class ProfissionalOnboardingForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ["nome", "sobrenome", "categoria", "telefone", "conselho", "numero_conselho"]

    def clean(self):
        cleaned = super().clean()
    
        if not cleaned.get("nome"):
            self.add_error("nome", "Informe seu nome.")
        if not cleaned.get("sobrenome"):
            self.add_error("sobrenome", "Informe seu sobrenome.")

        # Se informou conselho, exige o número
        if cleaned.get("conselho") and not cleaned.get("numero_conselho"):
            self.add_error("numero_conselho", "Informe o número do conselho.")

        return cleaned

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ["nome", "sobrenome"]