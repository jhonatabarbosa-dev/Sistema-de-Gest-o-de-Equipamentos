from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipamento
from .forms import EquipamentoForm

# 1. Tela de Listagem / Dashboard
def lista(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'meu_app/lista.html', {'equipamentos': equipamentos})

# 2. Tela de Cadastro
def cadastro(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')  # Redireciona de volta para a listagem ao salvar
    else:
        form = EquipamentoForm()
    return render(request, 'meu_app/cadastro.html', {'form': form})

# 3. Tela de Detalhes
def detalhes(request, id):
    equipamento = get_object_or_404(Equipamento, pk=id)
    return render(request, 'meu_app/detalhes.html', {'equipamento': equipamento})
