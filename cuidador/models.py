from django.db import models

class Cuidador(models.Model):
    CATEGORIA =[
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

    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=150),
    categoria = models.CharField(max_length=20, choices=CATEGORIA)
    conselho = models.CharField(max_length=40, choices=CONSELHOS_SAUDE)

