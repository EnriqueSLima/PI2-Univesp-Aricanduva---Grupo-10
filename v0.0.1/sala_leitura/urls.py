from django.urls import path
from .views import (
    cadastrar_usuario,
    cadastrar_produto,
    cadastrar_cliente,
    cadastrar_editora,
    cadastrar_locacao,
    cadastrar_locacao_itens,
    cadastrar_tipo_produto,
    landing_page,
    sucesso,
)

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('sucesso', sucesso, name='sucesso'),
    path('cadastrar-usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastrar-produto/', cadastrar_produto, name='cadastrar_produto'),
    path('cadastrar-tipo/', cadastrar_tipo_produto, name='cadastrar_tipo_produto'),
    path('cadastrar-cliente/', cadastrar_cliente, name='cadastrar_cliente'),
    path('cadastrar-editora/', cadastrar_editora, name='cadastrar_editora'),
    path('cadastrar-locacao/', cadastrar_locacao, name='cadastrar_locacao'),
    path('cadastrar-locacao-itens/', cadastrar_locacao_itens, name='cadastrar_locacao_itens'),
]
