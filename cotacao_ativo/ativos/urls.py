from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_ativo, name='cadastrar_ativo'),
    path('listagem/', views.listagem_ativos, name='listagem_ativos'),
]