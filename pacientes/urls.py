from django.urls import path, include
from.views import cadastrar_paciente
from . import views

urlpatterns = [
    path('cadastrar/', cadastrar_paciente, name='cadastrar_paciente'),
    path('pacientes/', include('pacientes.urls')),
    path('', views.lista_pacientes, name='lista_pacientes'),
]