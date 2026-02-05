from django.urls import path
from . import views

urlpatterns =  [
    path('welcome/', views.welcome, name='welcome'),
    path('onboarding/', views.onboarding_profissional, name="onboarding_profissional"),
    path('perfil/', views.perfil, name='perfil'),
]