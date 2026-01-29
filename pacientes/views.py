from django.shortcuts import render, redirect 
from .forms import PacienteForm
from django.http import HttpResponse
from django.contrib import messages
from .models import Paciente

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

def lista_paciente(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista_paciente.html', {
        'pacientes' : pacientes
    })