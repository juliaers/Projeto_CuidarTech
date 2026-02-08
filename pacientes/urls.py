from django.urls import path
from.views import cadastrar_paciente
from . import views

urlpatterns = [
    path('cadastrar/', cadastrar_paciente, name='cadastrar_paciente'),
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('<int:pk>/', views.paciente_detalhe, name='paciente_detalhe'),
    path('<int:pk>/editar/', views.editar_paciente, name='paciente_editar'),
]