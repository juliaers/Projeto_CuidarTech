from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

#Tabela no banco de dados do Django = Cadastro de pacientes

class Paciente(models.Model):
    nome_completo = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    diagnostico_principal = models.TextField()
    familiar_responsavel = models.CharField(max_length=100)
    contato_familiar = PhoneNumberField(blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.nome_completo
