from django.shortcuts import render
from .models import Profissional
from .forms import ProfissionalForm

'''def listar_profissionais_ativos(request):
    profissionais = Profissional.objects.filter(status='ativo')
    return render(request, 'profissionais/listar_cuidadores_ativos.html', {'profissionais': profissionais})

def inativar_profissional(request):
    profissionais = Profissional.objects.filter(status='ativo')
    return render(request)'''