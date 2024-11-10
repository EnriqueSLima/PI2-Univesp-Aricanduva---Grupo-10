from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm, LivroForm, EditoraForm, CategoriaForm, EmprestimoForm
from .models import Aluno, Livro, Editora, Categoria, Emprestimo
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse, HttpRequest
from django.db.models import Q
from urllib.parse import urlencode


def landing_page(request):
    return render(request, 'landing_page.html')

@login_required
def home_page(request):
    return render (request, "home_page.html")

#@login_required
#def consulta(request):
#    livros = Livro.objects.all()
#    alunos = Aluno.objects.all()
#    editoras = Editora.objects.all()
#    categorias = Categoria.objects.all()
#
#    return render(request, 'consulta.html', {
#        'livros': livros,
#        'alunos': alunos,
#        'editoras': editoras,
#        'categorias': categorias
#    })

#@login_required
#def consulta_modelo(request):
#    modelo = request.GET.get('modelo')
#    context = {'modelo': modelo}
#
#    if modelo == 'livros':
#        filtro = request.GET.get('filtro')
#        valor = request.GET.get('valor')
#        livros = Livro.objects.all()
#        
#        if filtro and valor:
#            if filtro == 'registro':
#                livros = livros.filter(registro__icontains=valor)
#            elif filtro == 'autor':
#                livros = livros.filter(autor__icontains=valor)
#            elif filtro == 'titulo':
#                livros = livros.filter(titulo__icontains=valor)
#            elif filtro == 'editora':
#                livros = livros.filter(editora__icontains=valor)
#        
#        context['livros'] = livros
#
#    elif modelo == 'alunos':
#        filtro = request.GET.get('filtro')
#        valor = request.GET.get('valor')
#        alunos = Aluno.objects.all()
#        
#        if filtro and valor:
#            if filtro == 'nome':
#                alunos = alunos.filter(nome__icontains=valor)
#            elif filtro == 'ra':
#                alunos = alunos.filter(ra__icontains=valor)
#            elif filtro == 'sexo':
#                alunos = alunos.filter(sexo__iexact=valor)
#        
#        context['alunos'] = alunos
#        context['is_sexo_filter'] = (filtro == 'sexo')  # Flag para o template
#
#    elif modelo == 'editoras':
#        busca_nome = request.GET.get('busca_nome')
#        editoras = Editora.objects.all()
#        
#        if busca_nome:
#            editoras = editoras.filter(nome__icontains=busca_nome)
#        
#        context['editoras'] = editoras
#
#    elif modelo == 'categorias':
#        busca_nome = request.GET.get('busca_nome')
#        categorias = Categoria.objects.all()
#        
#        if busca_nome:
#            categorias = categorias.filter(tipo__icontains=busca_nome)
#        
#        context['categorias'] = categorias
#    
#    return render(request, 'consulta.html', context)

@login_required
def consulta(request):
    return render(request, 'consulta.html')

@login_required
def lista_livros(request):
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
    
    return render(request, 'lista_livros.html', {'livros': livros})

@login_required
def lista_alunos(request):
    filtro = request.GET.get('filtro')
    valor = request.GET.get('valor')
    alunos = Aluno.objects.all()
    is_sexo_filter = False  # Flag para identificar se o filtro é 'sexo'

    if filtro and valor:
        if filtro == 'nome':
            alunos = alunos.filter(nome__icontains=valor)
        elif filtro == 'ra':
            alunos = alunos.filter(ra__icontains=valor)
        elif filtro == 'sexo':
            alunos = alunos.filter(sexo__iexact=valor)
            is_sexo_filter = True  # Ativa a flag para o filtro de sexo

    return render(request, 'lista_alunos.html', {'alunos': alunos, 'is_sexo_filter': is_sexo_filter})


@login_required
def lista_editoras(request):
    busca_nome = request.GET.get('busca_nome')
    editoras = Editora.objects.all()

    if busca_nome:
        editoras = editoras.filter(nome__icontains=busca_nome)
    
    return render(request, 'lista_editoras.html', {'editoras': editoras})

@login_required
def lista_categorias(request):
    busca_nome = request.GET.get('busca_nome')
    categorias = Categoria.objects.all()

    if busca_nome:
        categorias = categorias.filter(tipo__icontains=busca_nome)
    
    return render(request, 'lista_categorias.html', {'categorias': categorias})

@login_required
def lista_emprestimos(request):
    filtro = request.GET.get('filtro')
    valor = request.GET.get('valor')
    
    # Inicia a consulta de empréstimos com devolução confirmada
    historicos = Emprestimo.objects.filter(data_devolucao__isnull=False)

    if filtro and valor:
        if filtro == 'aluno':
            historicos = historicos.filter(aluno__nome__icontains=valor)
        elif filtro == 'titulo':
            historicos = historicos.filter(livro__titulo__icontains=valor)
        elif filtro == 'data_devolucao':
            try:
                # Tenta filtrar por data de devolução se o valor for uma data válida
                data_devolucao = timezone.datetime.strptime(valor, "%d/%m/%Y").date()
                historicos = historicos.filter(data_devolucao=data_devolucao)
            except ValueError:
                pass  # Caso não seja uma data válida, não aplica filtro
    
    # Carrega todas as opções de alunos e livros para o filtro
    alunos = Aluno.objects.all()
    livros = Livro.objects.all()

    return render(request, 'lista_emprestimos.html', {
        'historicos': historicos,
        'alunos': alunos,
        'livros': livros,
        'filtro': filtro,
        'valor': valor
    })

#def lista_livros(request):
#    return true
#
#def lista_alunos(request):
#    return true
#
#def lista_editoras(request):
#    return true
#
#def lista_categorias(request):
#    return true
#
#def lista_emprestimos(request):
#    return true

@login_required
def cadastro(request):
    form_livros = LivroForm()  # Cria uma instância de cada formulário
    form_alunos = AlunoForm()
    form_editoras = EditoraForm()
    form_categorias = CategoriaForm()
    modelo = request.GET.get('modelo')

@login_required
def cadastro(request):
    modelo = request.GET.get('modelo')  # Recebe o modelo atual

    # Inicializa formulários vazios
    form_livros = LivroForm()
    form_alunos = AlunoForm()
    form_editoras = EditoraForm()
    form_categorias = CategoriaForm()

    if request.method == 'POST':
        # Verifica qual formulário foi enviado
        if modelo == 'alunos':
            form_alunos = AlunoForm(request.POST)
            if form_alunos.is_valid():
                form_alunos.save()
                return redirect('cadastro')
        elif modelo == 'livros':
            form_livros = LivroForm(request.POST)
            if form_livros.is_valid():
                form_livros.save()
                return redirect('cadastro')
        elif modelo == 'editoras':
            form_editoras = EditoraForm(request.POST)
            if form_editoras.is_valid():
                form_editoras.save()
                return redirect('cadastro')
        elif modelo == 'categorias':
            form_categorias = CategoriaForm(request.POST)
            if form_categorias.is_valid():
                form_categorias.save()
                return redirect('cadastro')

    # Passa todos os formulários e o modelo selecionado para o contexto
    context = {
        'form_livros': form_livros,
        'form_alunos': form_alunos,
        'form_editoras': form_editoras,
        'form_categorias': form_categorias,
        'modelo': modelo
    }
    
    return render(request, 'cadastro.html', context)



#   *** Views serão deletadas   ***
#@login_required
#def cadastrar_livro(request):
#    if request.method == 'POST':
#        form = LivroForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('cadastro')  # Redirecionar após sucesso
#    else:
#        form = LivroForm()
#    
#    return render(request, 'cadastrar_livro.html', {'form': form})

#@login_required
#def cadastrar_aluno(request):
#    if request.method == 'POST':
#        form = AlunoForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('cadastro')  # Redirecionar após sucesso
#    else:
#        form = AlunoForm()
#    
#    return render(request, 'cadastrar_aluno.html', {'form': form})

#@login_required
#def cadastrar_editora(request):
#    if request.method == 'POST':
#        form = EditoraForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('cadastro')  # Redirecionar após sucesso
#    else:
#        form = EditoraForm()
#    
#    return render(request, 'cadastrar_editora.html', {'form': form})
#
#@login_required
#def cadastrar_categoria(request):
#    if request.method == 'POST':
#        form = CategoriaForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('cadastro')  # Redireciona após salvar
#    else:
#        form = CategoriaForm()
#
#    return render(request, 'cadastrar_categoria.html', {'form': form})


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
    emprestimos_hist = Emprestimo.objects.all()

    return render(request, 'emprestimo.html', {
        'form': form,
        'emprestimos': emprestimos_ativos,
        'historicos' : emprestimos_hist
    })

@login_required
def alterar_status_ativo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)

    # Alterna o status ativo
    emprestimo.ativo = not emprestimo.ativo
    emprestimo.save()

    return redirect('emprestimo')  # Redireciona após a alteração

def devolver_livro(request, emprestimo_id):
    # Obtenha o empréstimo com o ID fornecido ou 404 se não existir
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
    
    # Define a data_devolucao para a data atual e desativa o empréstimo
    emprestimo.data_devolucao = timezone.now().date()
    emprestimo.ativo = False
    emprestimo.save()

    return redirect('emprestimo')  # Substitua pelo nome correto da página de consulta


