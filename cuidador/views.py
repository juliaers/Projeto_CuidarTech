from django.shortcuts import render
from .models import Cuidador
from .forms import CuidadorForm

def listar_pacientes_ativos(request):
    cuidadores = Cuidador.objects.filter(status='ativo')
    return render(request, 'paciente/listar_cuidadores_ativos.html', {'cuidadores': cuidadores})

def cadastrar_paciente(request):
    if request.method == 'POST':
        form = CuidadorForm(request.POST)