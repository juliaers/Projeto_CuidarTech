from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import CadastroForm

def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Login automático após cadastro
            login(request, user)

            messages.success(request, "Conta criada com sucesso")
            return redirect("perfil") # Redireciona para o perfil
        else:
            messages.error(request, "Revise os campos e tente novamente.")
    else:
        form = CadastroForm()

    return render(request, "accounts/cadastro.html", {"form": form})