from django.urls import path
from . import views

urlpatterns = [
    path('criar_tipo_produto/', views.criar_tipo_produto, name='criar_tipo_produto'),
    path('tipo_produto_sucesso/', views.sucesso, name='tipo_produto_sucesso'),  # Página de sucesso (opcional)
]
