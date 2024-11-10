from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

from .views import (
    landing_page,
    home_page,
    consulta,
    consulta_modelo,
    cadastro,
    #cadastrar_livro,
    #cadastrar_aluno,
    #cadastrar_editora,
    #cadastrar_categoria,
    emprestimo,
    alterar_status_ativo,
    devolver_livro,
    historico_emprestimos
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', landing_page, name='landing_page'),
    path('home/', home_page, name='home_page'),
    path('consulta/', consulta, name='consulta'),
    path('consulta_modelo/', consulta_modelo, name='consulta_modelo'),
    path('cadastro/', cadastro, name='cadastro'),
    #path('cadastrar-livro/', cadastrar_livro, name='cadastrar_livro'),
    #path('cadastrar-categoria/', cadastrar_categoria, name='cadastrar_categoria'),
    #path('cadastrar-aluno/', cadastrar_aluno, name='cadastrar_aluno'),
    #path('cadastrar-editora/', cadastrar_editora, name='cadastrar_editora'),
    path('emprestimo/', emprestimo, name='emprestimo'),
    path('alterar_status_ativo/<int:emprestimo_id>/', alterar_status_ativo, name='alterar_status_ativo'),
    path('emprestimo/devolver/<int:emprestimo_id>/', devolver_livro, name='devolver_livro'),
    path('historico-emprestimos/', historico_emprestimos, name='historico_emprestimos'),
]
