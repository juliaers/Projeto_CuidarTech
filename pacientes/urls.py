from django.urls import path
from.views import cadastrar_paciente

urlpatterns = [
    path('cadastrar/', cadastrar_paciente,
name='cadastrar_paciente'),
]