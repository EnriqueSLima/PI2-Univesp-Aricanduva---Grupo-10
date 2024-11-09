from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm, LivroForm, EditoraForm, CategoriaForm, EmprestimoForm
from .models import Aluno, Livro, Editora, Categoria, Emprestimo
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def landing_page(request):
    return render(request, 'landing_page.html')

@login_required
def consulta(request):
    livros = Livro.objects.all()
    alunos = Aluno.objects.all()
    editoras = Editora.objects.all()
    categorias = Categoria.objects.all()

    return render(request, 'consulta.html', {
        'livros': livros,
        'alunos': alunos,
        'editoras': editoras,
        'categorias': categorias
    })


@login_required
def consulta_modelo(request):
    modelo = request.GET.get('modelo')
    if modelo == 'livros':
        return redirect('lista_livros')
    elif modelo == 'alunos':
        return redirect('lista_alunos')
    elif modelo == 'editoras':
        return redirect('lista_editoras')
    elif modelo == 'categorias':
        return redirect('lista_categorias')
    else:
        return redirect('consulta')  # Redireciona de volta se não houver modelo correspondente

@login_required
def lista_livros(request):
    filtro = request.GET.get('filtro')
    valor = request.GET.get('valor')
    livros = Livro.objects.all()
    
    if filtro and valor:
        filtros = {
            'tombo': 'tombo__icontains',
            'registro': 'registro__icontains',
            'autor': 'autor__icontains',
            'titulo': 'titulo__icontains',
            'editora': 'editora__icontains',
        }
        if filtro in filtros:
            livros = livros.filter(**{filtros[filtro]: valor})
    
    return render(request, 'lista_livros.html', {'livros': livros})


@login_required
def lista_alunos(request):
    busca_nome = request.GET.get('busca_nome', '')
    busca_ra = request.GET.get('busca_ra', '')
    busca_sexo = request.GET.get('busca_sexo', '')

    alunos = Aluno.objects.all()

    # Filtros
    if busca_nome:
        alunos = alunos.filter(nome__icontains=busca_nome)
    if busca_ra:
        alunos = alunos.filter(ra__icontains=busca_ra)
    if busca_sexo:
        alunos = alunos.filter(sexo=busca_sexo)

    return render(request, 'lista_alunos.html', {'alunos': alunos})


@login_required
def lista_editoras(request):
    busca_nome = request.GET.get('busca_nome', '')
    editoras = Editora.objects.all()
    
    if busca_nome:
        editoras = editoras.filter(nome__icontains=busca_nome)
    
    return render(request, 'lista_editoras.html', {'editoras': editoras})


@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()  # Recupera todos os clientes do banco de dados
    busca_nome = request.GET.get('busca_nome', '')
    
    if busca_nome:
        categorias = categorias.filter(nome__icontains=busca_nome)
    
    return render(request, 'lista_categorias.html', {'categorias': categorias})

@login_required
def cadastro(request):
    form_livros = LivroForm()  # Crie uma instância de cada formulário que você deseja
    form_alunos = AlunoForm()
    form_editoras = EditoraForm()
    form_categorias = CategoriaForm()

    context = {
        'form_livros': form_livros,
        'form_alunos': form_alunos,
        'form_editoras': form_editoras,
        'form_categorias': form_categorias,
    }
    return render(request, 'cadastro.html', context)


@login_required
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')  # Redirecionar após sucesso
    else:
        form = LivroForm()
    
    return render(request, 'cadastrar_livro.html', {'form': form})

@login_required
def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')  # Redirecionar após sucesso
    else:
        form = AlunoForm()
    
    return render(request, 'cadastrar_aluno.html', {'form': form})

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

@login_required
def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')  # Redireciona após salvar
    else:
        form = CategoriaForm()

    return render(request, 'cadastrar_categoria.html', {'form': form})

@login_required
def emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o empréstimo
            return redirect('emprestimo')  # Redireciona após salvar
    else:
        form = EmprestimoForm()

    # Filtra os empréstimos que ainda estão ativos
    emprestimos_ativos = Emprestimo.objects.filter(ativo=True)

    return render(request, 'emprestimo.html', {
        'form': form,
        'emprestimos': emprestimos_ativos,
    })

from django.shortcuts import get_object_or_404, redirect
from .models import Emprestimo

@login_required
def alterar_status_ativo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)

    # Alterna o status ativo
    emprestimo.ativo = not emprestimo.ativo
    emprestimo.save()

    return redirect('emprestimo')  # Redireciona após a alteração
