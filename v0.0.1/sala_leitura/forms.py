from django import forms
from .models import Aluno, Livro, Editora, Categoria, Emprestimo

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'ra', 'sexo', 'ativo']  # Campos do modelo a serem incluídos no formulário
        widgets = {
            'sexo': forms.Select(choices=Aluno.SEXO_CHOICES),  # Para garantir que o campo 'sexo' seja exibido como um select
        }

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['tombo', 'registro', 'autor', 'titulo', 'procedencia', 'exemplar', 
                  'colecao', 'edicao', 'ano', 'vol', 'editora', 'observacao', 'aquisicao']
        widgets = {
            'aquisicao': forms.Select(choices=Livro.AQUISICAO_CHOICES),  # Garantindo o campo 'aquisicao' como select
        }

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome', 'email', 'fone', 'ativo']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['tipo']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['aluno', 'livro']  # Campos que o usuário irá preencher no formulário (o resto é calculado automaticamente)
        widgets = {
            'aluno': forms.Select(),  # Campo para selecionar o aluno
            'livro': forms.Select(),  # Campo para selecionar o livro
        }