from django.shortcuts import render, redirect, get_object_or_404
from .forms import TipoProdutoForm, UsuariosForm, ProdutosForm, ClienteForm, EditoraForm, LocacaoForm, LocacaoItensForm
from .models import Cliente, Produtos, Editora, TipoProduto, Locacao, LocacaoItens
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, 'landing_page.html')

def login(request):
    return render(request, 'login.html')

@login_required
def consulta(request):
    return render(request, 'consulta.html')

@login_required
def consulta_modelo(request):
    modelo = request.GET.get('modelo')
    if modelo == 'produtos':
        return redirect('lista_produtos')
    elif modelo == 'clientes':
        return redirect('lista_clientes')
    elif modelo == 'editoras':
        return redirect('lista_editoras')
    elif modelo == 'categorias':
        return redirect('lista_tipo_prods')
    else:
        return redirect('consulta')  # Redireciona de volta se não houver modelo correspondente

@login_required
def lista_produtos(request):
    produtos = Produtos.objects.all()  # Recupera todos os produtos do banco de dados
    return render(request, 'lista_produtos.html', {'produtos': produtos})

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()  # Recupera todos os clientes do banco de dados
    return render(request, 'lista_clientes.html', {'clientes': clientes})

@login_required
def lista_editoras(request):
    editoras = Editora.objects.all()  # Recupera todos os produtos do banco de dados
    return render(request, 'lista_editoras.html', {'editoras': editoras})

@login_required
def lista_tipo_prods(request):
    categorias = TipoProduto.objects.all()  # Recupera todos os clientes do banco de dados
    return render(request, 'lista_tipo_prods.html', {'categorias': categorias})

@login_required
def cadastro(request):
    form_produto = ProdutosForm()  # Crie uma instância de cada formulário que você deseja
    form_cliente = ClienteForm()
    form_editora = EditoraForm()
    form_categoria = TipoProdutoForm()

    context = {
        'form_produto': form_produto,
        'form_cliente': form_cliente,
        'form_editora': form_editora,
        'form_categoria': form_categoria,
    }
    return render(request, 'cadastro.html', context)

@login_required
def cadastrar_tipo_produto(request):
    if request.method == 'POST':
        form = TipoProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')  # Redireciona após salvar
    else:
        form = TipoProdutoForm()

    return render(request, 'cadastrar_tipo_produto.html', {'form': form})

@login_required
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')  # Redirecionar após sucesso
    else:
        form = UsuariosForm()
    
    return render(request, 'cadastrar_usuario.html', {'form': form})

@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')  # Redirecionar após sucesso
    else:
        form = ProdutosForm()
    
    return render(request, 'cadastrar_produto.html', {'form': form})

@login_required
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')  # Redirecionar após sucesso
    else:
        form = ClienteForm()
    
    return render(request, 'cadastrar_cliente.html', {'form': form})

@login_required
def cadastrar_editora(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')  # Redirecionar após sucesso
    else:
        form = EditoraForm()
    
    return render(request, 'cadastrar_editora.html', {'form': form})

def emprestimo(request):
    if request.method == "POST":
        # Processa o formulário
        formulario1 = LocacaoForm(request.POST)
        formulario2 = LocacaoItensForm(request.POST)

        if formulario1.is_valid() and formulario2.is_valid():
            # Salve os dados conforme necessário
            formulario1.save()
            formulario2.save()
            return redirect('emprestimo')

    else:
        formulario1 = LocacaoForm()
        formulario2 = LocacaoItensForm()

    emprestimos_ativos = Locacao.objects.all()  # Ajuste conforme sua lógica

    return render(request, 'emprestimo.html', {
        'formulario1': formulario1,
        'formulario2': formulario2,
        'emprestimos': emprestimos_ativos
    })

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
