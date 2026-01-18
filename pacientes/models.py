from django.db import models

#Tabela no banco de dados do Django = Cadastro de pacientes

class Paciente(models.Model):
    nome_completo = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    diagnostico_principal = models.TextField()
    familiar_responsavel = models.CharField(max_length=200)
    contato_familiar = models.CharField(max_length=50)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.nome_completo
