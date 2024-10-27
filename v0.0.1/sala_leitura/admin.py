from django.contrib import admin
from .models import Editora, Locacao, LocacaoItens, Cliente, Produtos, TipoProduto, Usuarios

# Register your models here.
admin.site.register(Editora)
admin.site.register(Locacao)
admin.site.register(LocacaoItens)
admin.site.register(Cliente)
admin.site.register(Produtos)
admin.site.register(TipoProduto)
admin.site.register(Usuarios)
