from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

from .views import (
    landing_page,
    login,
    consulta,
    consulta_modelo,
    lista_livros,
    lista_alunos,
    lista_editoras,
    lista_categorias,
    cadastro,
    cadastrar_livro,
    cadastrar_aluno,
    cadastrar_editora,
    cadastrar_categoria,
    emprestimo,
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', landing_page, name='landing_page'),
    path('consulta/', consulta, name='consulta'),
    path('consulta_modelo/', consulta_modelo, name='consulta_modelo'),
    path('livros/', lista_livros, name='lista_livros'),
    path('alunos/', lista_alunos, name='lista_alunos'),
    path('editoras/', lista_editoras, name='lista_editoras'),
    path('categorias/', lista_categorias, name='lista_categorias'),
    path('cadastro/', cadastro, name='cadastro'),
    path('cadastrar-livro/', cadastrar_livro, name='cadastrar_livro'),
    path('cadastrar-categoria/', cadastrar_categoria, name='cadastrar_categoria'),
    path('cadastrar-aluno/', cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastrar-editora/', cadastrar_editora, name='cadastrar_editora'),
    path('emprestimo/', emprestimo, name='emprestimo'),
]
