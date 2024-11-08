from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

from .views import (
    landing_page,
    login,
    consulta,
    consulta_modelo,
    lista_produtos,
    lista_clientes,
    lista_editoras,
    lista_tipo_prods,
    cadastro,
    cadastrar_usuario,
    cadastrar_produto,
    cadastrar_cliente,
    cadastrar_editora,
    cadastrar_locacao,
    emprestimo,
    cadastrar_locacao_itens,
    cadastrar_tipo_produto,
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', landing_page, name='landing_page'),
    path('consulta/', consulta, name='consulta'),
    path('consulta_modelo/', consulta_modelo, name='consulta_modelo'),
    path('produtos/', lista_produtos, name='lista_produtos'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('editoras/', lista_editoras, name='lista_editoras'),
    path('categorias/', lista_tipo_prods, name='lista_tipo_prods'),
    path('cadastro/', cadastro, name='cadastro'),
    path('cadastrar-usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastrar-produto/', cadastrar_produto, name='cadastrar_produto'),
    path('cadastrar-tipo/', cadastrar_tipo_produto, name='cadastrar_tipo_produto'),
    path('cadastrar-cliente/', cadastrar_cliente, name='cadastrar_cliente'),
    path('cadastrar-editora/', cadastrar_editora, name='cadastrar_editora'),
    path('emprestimo/', emprestimo, name='emprestimo'),
    path('cadastrar-locacao/', cadastrar_locacao, name='cadastrar_locacao'),
    path('cadastrar-locacao-itens/', cadastrar_locacao_itens, name='cadastrar_locacao_itens'),
]
