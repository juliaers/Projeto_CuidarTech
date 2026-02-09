from django.shortcuts import render, redirect 
from .forms import PacienteForm

from django.http import HttpResponse
from django.contrib import messages
from .models import Paciente
from django.shortcuts import get_object_or_404

# Função temporária para a página inicial
def home(request):
    return HttpResponse("Página inicial do sistema CuidarTech.")

# Função para cadastrar um novo paciente
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

# Função para listar os pacientes cadastrados
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista_pacientes.html', {
        'pacientes' : pacientes
    })

# Função para exibir os detalhes de um paciente específico
def paciente_detalhe(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    print(paciente.nome_completo)
    return render(request, 'pacientes/paciente_detalhe.html', {
        'paciente': paciente
    })

# Função para editar os detalhes de um paciente específico
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
    
    return render(request, 'pacientes/cadastro.html', {
        'form': form,
        'paciente': paciente
    })