from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib  import messages
from .models import Profissional
from .forms import ProfissionalForm, ProfissionalOnboardingForm

@login_required
def welcome(request):
    profissional = request.user.profissional

    # Se já fez onboarding, não volta para welcome
    if profissional.onboarding_concluido:
        messages.info(request, "Você já concluiu seu cadastro.")
        return redirect("dashboard")
    
    if request.session.pop(request,"msg_conta_criada", False):
        messages.success(request, "Conta criada com sucesso!")
    
    return render(request, "profissionais/welcome.html")

@login_required
def onboarding_profissional(request):
    profissional = request.user.profissional

    if profissional.onboarding_concluido:
        messages.info(request, "Seu cadastro já foi concluído.")
        return redirect("dashboard")
    
    if request.method == "POST":
        form = ProfissionalOnboardingForm(request.POST, instance=profissional)

        if form.is_valid():
            prof = form.save(commit=False)
            prof.onboarding_concluido = True
            prof.save()

            messages.success(request, "Perfil atualizado.")
            return redirect("dashboard")
        
        messages.error(request, "Revise os campos.")
    else:
        form = ProfissionalOnboardingForm(instance=profissional)
    
    return render(request, "profissionais/onboarding_profissional.html", {"form": form})


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