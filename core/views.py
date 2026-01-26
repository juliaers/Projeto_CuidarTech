from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

@login_required
def dashboard(request):
    prof = request.user.profissional
    if not prof.nome or not prof.sobrenome:
        return redirect("perfil")
    return render(request, "dashboard.html")
