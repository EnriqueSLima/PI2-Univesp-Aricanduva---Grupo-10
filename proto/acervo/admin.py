from django.contrib import admin
from .models import Livro, Leitor, Emprestimo

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'quantidade_disponivel', 'quantidade_total')

@admin.register(Leitor)
class LeitorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'leitor', 'data_emprestimo', 'data_devolucao', 'devolvido')
    list_filter = ('devolvido', 'data_emprestimo')
