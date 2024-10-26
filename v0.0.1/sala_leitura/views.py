from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import TipoProdutoForm

def criar_tipo_produto(request):
    if request.method == 'POST':
        form = TipoProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipo_produto_sucesso')  # Redireciona após salvar
    else:
        form = TipoProdutoForm()

    return render(request, 'criar_tipo_produto.html', {'form': form})

def sucesso(request):
    return render(request, 'sucesso.html', {'mensagem': 'Tipo de Produto criado com sucesso!'})
