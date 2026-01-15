from django.shortcuts import render
from .models import Cuidador
from .forms import CuidadorForm

def listar_pacientes_ativos(request):
    pacientes = Paciente.objects.filter(status='ativo')
    return render(request, 'paciente/listar_pacientes_ativos.html'), ('pacientes': pacientes)

def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)