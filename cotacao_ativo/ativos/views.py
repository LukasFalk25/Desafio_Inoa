from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AtivoForm
from .models import Ativo

def home(request):
    return HttpResponse("Página inicial de cotações")

def cadastrar_ativo(request):
    if request.method == 'POST':
        form = AtivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_ativos')
    else:
        form = AtivoForm()

    return render(request, 'ativos/cadastrar_ativo.html', {'form': form})
    
def listagem_ativos(request):
    ativos = Ativo.objects.all()
    return render(request, 'ativos/listagem_ativos.html', {'ativos': ativos})