from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib  import messages
from .models import Profissional
from .forms import ProfissionalForm

'''def listar_profissionais_ativos(request):
    profissionais = Profissional.objects.filter(status='ativo')
    return render(request, 'profissionais/listar_cuidadores_ativos.html', {'profissionais': profissionais})

def inativar_profissional(request):
    profissionais = Profissional.objects.filter(status='ativo')
    return render(request)'''

@login_required
def perfil(request):
    profissional = request.user.profissional

    if request.method == "POST":
        form = ProfissionalForm(request.POST, instance=profissional)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado!")
            return redirect("perfil")
        else:
            messages.error(request, "Revise os campos e tente novamente.")
    else:
        form = ProfissionalForm(instance=profissional)

    return render(request, "profissionais/perfil.html", {"form": form})