from django.shortcuts import render, redirect 
from .forms import PacienteForm

from django.http import HttpResponse
from django.contrib import messages
from .models import Paciente
from django.shortcuts import get_object_or_404

def home(request):
    return HttpResponse("Página inicial do sistema CuidarTech.")

def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente cadastrado com sucesso!')
            return redirect('cadastrar_paciente')
    else:
        form = PacienteForm()
    
    return render(request, 'pacientes/cadastro.html',
    {'form':form})

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista_pacientes.html', {
        'pacientes' : pacientes
    })

def paciente_detalhe(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    print(paciente.nome_completo)
    return render(request, 'pacientes/paciente_detalhe.html', {
        'paciente': paciente
    })

def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente atualizado com sucesso!')
            return redirect('paciente_detalhe', pk=paciente.pk)
    else:
        form = PacienteForm(instance=paciente)
    
    return render(request, 'pacientes/editar_paciente.html', {
        'form': form,
        'paciente': paciente
    })