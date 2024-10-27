from django.shortcuts import render, redirect
from .forms import TipoProdutoForm, UsuariosForm, ProdutosForm, ClienteForm, EditoraForm, LocacaoForm, LocacaoItensForm
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, 'landing_page.html')

# VIEW DE SUCESSO
def sucesso(request):
    return render(request, 'sucesso.html', {'mensagem': 'Cadastro criado com sucesso!'})

# VIEW DE CADASTRO DE USUARIO

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_usuario')  # Redirecionar após sucesso
    else:
        form = UsuariosForm()
    
    return render(request, 'cadastrar_usuario.html', {'form': form})

# VIEW DE CADASTRO DE PRODUTO
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso.html')  # Redirecionar após sucesso
    else:
        form = ProdutosForm()
    
    return render(request, 'cadastrar_produto.html', {'form': form})

# VIEW DE CADASTRO DE CLIENTE
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso.html')  # Redirecionar após sucesso
    else:
        form = ClienteForm()
    
    return render(request, 'cadastrar_cliente.html', {'form': form})

# VIEW DE CADASTRO DE EDITORA
def cadastrar_editora(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso.html')  # Redirecionar após sucesso
    else:
        form = EditoraForm()
    
    return render(request, 'cadastrar_editora.html', {'form': form})

# VIEW DE LOCAÇÃO
def cadastrar_locacao(request):
    if request.method == 'POST':
        form = LocacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso.html')  # Redirecionar após sucesso
    else:
        form = LocacaoForm()
    
    return render(request, 'cadastrar_locacao.html', {'form': form})

# VIEW DE ITENS DE LOCAÇÃO
def cadastrar_locacao_itens(request):
    if request.method == 'POST':
        form = LocacaoItensForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso.html')  # Redirecionar após sucesso
    else:
        form = LocacaoItensForm()
    
    return render(request, 'cadastrar_locacao_itens.html', {'form': form})

#VIEW DE CADASTRO DE TIPO DE PRODUTO
def cadastrar_tipo_produto(request):
    if request.method == 'POST':
        form = TipoProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # Redireciona após salvar
    else:
        form = TipoProdutoForm()

    return render(request, 'cadastrar_tipo_produto.html', {'form': form})