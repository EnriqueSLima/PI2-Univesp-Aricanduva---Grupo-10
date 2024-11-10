from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

from .views import (
    landing_page,
    home_page,
    consulta,
    #consulta_modelo,
    cadastro,
    lista_livros,
    lista_alunos,
    lista_editoras,
    lista_categorias,
    lista_emprestimos,
    emprestimo,
    alterar_status_ativo,
    devolver_livro,
    #historico_emprestimos
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', landing_page, name='landing_page'),
    path('home/', home_page, name='home_page'),
    path('consulta/', consulta, name='consulta'),
    path('lista_livros/', lista_livros, name='lista_livros'),
    path('lista_alunos/', lista_alunos, name='lista_alunos'),
    path('lista_editoras/', lista_editoras, name='lista_editoras'),
    path('lista_categorias/', lista_categorias, name='lista_categorias'),
    path('lista_emprestimos/', lista_emprestimos, name='lista_emprestimos'),
    #path('consulta_modelo/', consulta_modelo, name='consulta_modelo'),
    path('cadastro/', cadastro, name='cadastro'),
    path('emprestimo/', emprestimo, name='emprestimo'),
    path('alterar_status_ativo/<int:emprestimo_id>/', alterar_status_ativo, name='alterar_status_ativo'),
    path('emprestimo/devolver/<int:emprestimo_id>/', devolver_livro, name='devolver_livro'),
    #path('historico-emprestimos/', historico_emprestimos, name='historico_emprestimos'),
]
