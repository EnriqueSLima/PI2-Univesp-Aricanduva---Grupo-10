from django.urls import path
from .views import LivroListView, LivroDetailView, EmprestimoCreateView, EmprestimoListView

urlpatterns = [
    path('livros/', LivroListView.as_view(), name='livros_lista'),
    path('livros/<int:pk>/', LivroDetailView.as_view(), name='livro_detalhe'),
    path('emprestimos/novo/', EmprestimoCreateView.as_view(), name='novo_emprestimo'),
    path('emprestimos/', EmprestimoListView.as_view(), name='emprestimos_lista'),
]
