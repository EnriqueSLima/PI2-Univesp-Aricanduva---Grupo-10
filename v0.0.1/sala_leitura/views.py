from django.shortcuts import render, redirect
from .forms import TipoProdutoForm, UsuariosForm, ProdutosForm, ClienteForm, EditoraForm, LocacaoForm, LocacaoItensForm
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, 'landing_page.html')

def login(request):
    return render(request, 'login.html')

@login_required
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_usuario')  # Redirecionar após sucesso
    else:
        form = UsuariosForm()
    
    return render(request, 'cadastrar_usuario.html', {'form': form})

@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_produto')  # Redirecionar após sucesso
    else:
        form = ProdutosForm()
    
    return render(request, 'cadastrar_produto.html', {'form': form})

@login_required
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_cliente')  # Redirecionar após sucesso
    else:
        form = ClienteForm()
    
    return render(request, 'cadastrar_cliente.html', {'form': form})

@login_required
def cadastrar_editora(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_editora')  # Redirecionar após sucesso
    else:
        form = EditoraForm()
    
    return render(request, 'cadastrar_editora.html', {'form': form})

@login_required
def cadastrar_locacao(request):
    if request.method == 'POST':
        form = LocacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_locacao')  # Redirecionar após sucesso
    else:
        form = LocacaoForm()
    
    return render(request, 'cadastrar_locacao.html', {'form': form})

@login_required
def cadastrar_locacao_itens(request):
    if request.method == 'POST':
        form = LocacaoItensForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_locacao_itens')  # Redirecionar após sucesso
    else:
        form = LocacaoItensForm()
    
    return render(request, 'cadastrar_locacao_itens.html', {'form': form})

@login_required
def cadastrar_tipo_produto(request):
    if request.method == 'POST':
        form = TipoProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_tipo_produto')  # Redireciona após salvar
    else:
        form = TipoProdutoForm()

    return render(request, 'cadastrar_tipo_produto.html', {'form': form})

def cadastro(request):
    cliente_form = ClienteForm()
    editora_form = EditoraForm()
    categoria_form = TipoProdutoForm()
    produto_form = ProdutosForm()

    return render(request, 'cadastro.html', {
        'cliente_form': cliente_form,
        'editora_form': editora_form,
        'categoria_form': categoria_form,
        'produto_form': produto_form,
    })
