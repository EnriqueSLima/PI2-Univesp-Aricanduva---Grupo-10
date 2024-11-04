from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

from .views import (
    cadastrar_usuario,
    cadastrar_produto,
    cadastrar_cliente,
    cadastrar_editora,
    cadastrar_locacao,
    cadastrar_locacao_itens,
    cadastrar_tipo_produto,
    landing_page,
    login,
)

urlpatterns = [
    #path('', lambda request: redirect('login')),  # Redireciona para a view de login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', landing_page, name='landing_page'),
    path('cadastrar-usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastrar-produto/', cadastrar_produto, name='cadastrar_produto'),
    path('cadastrar-tipo/', cadastrar_tipo_produto, name='cadastrar_tipo_produto'),
    path('cadastrar-cliente/', cadastrar_cliente, name='cadastrar_cliente'),
    path('cadastrar-editora/', cadastrar_editora, name='cadastrar_editora'),
    path('cadastrar-locacao/', cadastrar_locacao, name='cadastrar_locacao'),
    path('cadastrar-locacao-itens/', cadastrar_locacao_itens, name='cadastrar_locacao_itens'),
]
