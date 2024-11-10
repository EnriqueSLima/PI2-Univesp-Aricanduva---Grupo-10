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
    context = {'modelo': modelo}

    if modelo == 'livros':
        filtro = request.GET.get('filtro')
        valor = request.GET.get('valor')
        livros = Livro.objects.all()
        
        if filtro and valor:
            if filtro == 'registro':
                livros = livros.filter(registro__icontains=valor)
            elif filtro == 'autor':
                livros = livros.filter(autor__icontains=valor)
            elif filtro == 'titulo':
                livros = livros.filter(titulo__icontains=valor)
            elif filtro == 'editora':
                livros = livros.filter(editora__icontains=valor)
        
        context['livros'] = livros

    elif modelo == 'alunos':
        filtro = request.GET.get('filtro')
        valor = request.GET.get('valor')
        alunos = Aluno.objects.all()
        
        if filtro and valor:
            if filtro == 'nome':
                alunos = alunos.filter(nome__icontains=valor)
            elif filtro == 'ra':
                alunos = alunos.filter(ra__icontains=valor)
            elif filtro == 'sexo':
                alunos = alunos.filter(sexo__iexact=valor)
        
        context['alunos'] = alunos
        context['is_sexo_filter'] = (filtro == 'sexo')  # Flag para o template

    elif modelo == 'editoras':
        busca_nome = request.GET.get('busca_nome')
        editoras = Editora.objects.all()
        
        if busca_nome:
            editoras = editoras.filter(nome__icontains=busca_nome)
        
        context['editoras'] = editoras

    elif modelo == 'categorias':
        busca_nome = request.GET.get('busca_nome')
        categorias = Categoria.objects.all()
        
        if busca_nome:
            categorias = categorias.filter(tipo__icontains=busca_nome)
        
        context['categorias'] = categorias

    return render(request, 'consulta.html', context)

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

@login_required
def alterar_status_ativo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)

    # Alterna o status ativo
    emprestimo.ativo = not emprestimo.ativo
    emprestimo.save()

    return redirect('emprestimo')  # Redireciona após a alteração
