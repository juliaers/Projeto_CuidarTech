from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.db import models
# Definição de User
User = get_user_model()


class ContextoAtuacao(models.TextChoices):
    HOSPITALAR = "HOSP", "Hospitalar"
    DOMICILIAR = "DOM", "Domiciliar"
    CLINICA = "CLI", "Clinica"

class Profissional(models.Model):
    CATEGORIA = [
        ('cuidador', 'Cuidador(a)'),
        ('enfermeiro', 'Enfermeiro(a)')
    ]
    
    CONSELHOS_SAUDE = [
    ("CRBM", "CRBM - Biomedicina"),
    ("CRM", "CRM - Medicina"),
    ("COREN", "COREN - Enfermagem"),
    ("CRO", "CRO - Odontologia"),
    ("CRF", "CRF - Farmácia"),
    ("CRP", "CRP - Psicologia"),
    ("CREFITO", "CREFITO - Fisioterapia / Terapia Ocupacional"),
    ("CRBio", "CRBio - Biologia"),
    ("CREFONO", "CREFONO - Fonoaudiologia"),
    ("CRN", "CRN - Nutrição"),
    ("CRESS", "CRESS - Serviço Social"),
    ("CREF", "CREF - Educação Física"),
    ("CRQ", "CRQ - Química"),
    ("OUTRO", "Outro / Não se aplica"),
]
    STATUS = [
        ("ativo", "Ativo"),
        ("inativo", "Inativo")
    ]

    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=150),
    categoria = models.CharField(max_length=20, choices=CATEGORIA)
    conselho = models.CharField(max_length=40, choices=CONSELHOS_SAUDE)
    numero_conselho = models.CharField(max_length=30)
    status = models
    # Define o contexto de atuação como "Domiciliar"
    ContextoAtuacao = models.CharField(max_length=5, default="DOM", editable=False)


