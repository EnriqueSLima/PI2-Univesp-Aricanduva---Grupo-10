from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Livro, Emprestimo
from .forms import EmprestimoForm

# View para listar todos os livros
class LivroListView(ListView):
    model = Livro
    template_name = 'livros/livro_list.html'
    context_object_name = 'livros'

# View para detalhes de um livro específico
class LivroDetailView(DetailView):
    model = Livro
    template_name = 'livros/livro_detail.html'
    context_object_name = 'livro'

# View para registrar um novo empréstimo
class EmprestimoCreateView(CreateView):
    model = Emprestimo
    form_class = EmprestimoForm
    template_name = 'emprestimos/emprestimo_form.html'
    success_url = reverse_lazy('emprestimos_lista')

    def form_valid(self, form):
        # Atualiza a quantidade disponível do livro ao registrar o empréstimo
        livro = form.cleaned_data['livro']
        if livro.quantidade_disponivel > 0:
            livro.quantidade_disponivel -= 1
            livro.save()
        return super().form_valid(form)

# View para listar todos os empréstimos
class EmprestimoListView(ListView):
    model = Emprestimo
    template_name = 'emprestimos/emprestimo_list.html'
    context_object_name = 'emprestimos'

