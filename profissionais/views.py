from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib  import messages
from .models import Profissional
from .forms import ProfissionalForm, ProfissionalOnboardingForm

@login_required
def onboarding(request):
    profissional = request.user.profissional

    if profissional.onboarding_concluido:
        messages.info(request, "Seu cadastro já foi concluído.")
        return redirect("dashboard")
    
    if request.method == "POST":
        form = ProfissionalOnboardingForm(request.POST, instance=profissional)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado.")
            return redirect(request, "Revise os campos.")
        messages.error(request, "Revise os campos.")
    else:
        form = ProfissionalForm(instance=profissional)
    return render(request, "profissionais/onboarding.html", {"form": form})


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