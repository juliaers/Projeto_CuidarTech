from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

@login_required
def dashboard(request):
    profissional = request.user.profissional
    if not profissional.onboarding_concluido:
        return redirect("onboarding_profissional")
    return render(request, "dashboard.html")
