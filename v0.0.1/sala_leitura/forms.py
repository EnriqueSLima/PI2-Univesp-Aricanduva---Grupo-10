from django import forms
from .models import Aluno, Livro, Editora, Categoria, Emprestimo

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'ra', 'sexo', 'ativo']  # Campos do modelo a serem incluídos no formulário
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome'}),
            'ra': forms.TextInput(attrs={'placeholder': 'Digite o RA'}),
            'sexo': forms.Select(choices=Aluno.SEXO_CHOICES, attrs={'class': 'form-control mr-2'}),  # Para garantir que o campo 'sexo' seja exibido como um select
            'ativo': forms.Select(choices=Editora.ATIVO_CHOICES, attrs={'class': 'form-control mr-2'}),
        }

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['tombo', 'registro', 'autor', 'titulo', 'procedencia', 'exemplar', 
                  'colecao', 'edicao', 'ano', 'vol', 'editora', 'observacao', 'aquisicao']
        widgets = {
            'tombo': forms.TextInput(attrs={'placeholder': 'XX/XX/XX'}),
            'registro': forms.TextInput(attrs={'placeholder': 'Digite o registro'}),            
            'autor': forms.TextInput(attrs={'placeholder': 'Digite o(a) autor(a)'}),
            'titulo': forms.TextInput(attrs={'placeholder': 'Digite o titulo'}),
            'procedencia': forms.TextInput(attrs={'placeholder': 'Digite a procedência'}),
            'exemplar': forms.TextInput(attrs={'placeholder': 'Digite o exemplar'}),
            'colecao': forms.TextInput(attrs={'placeholder': 'Digite a coleção'}),
            'edicao': forms.TextInput(attrs={'placeholder': 'Digite a edição'}),
            'ano': forms.TextInput(attrs={'placeholder': 'Digite o ano'}),
            'vol': forms.TextInput(attrs={'placeholder': 'Digite o volume'}),
            'editora': forms.TextInput(attrs={'placeholder': 'Digite a editora'}),
            'aquisicao': forms.Select(choices=Livro.AQUISICAO_CHOICES, attrs={'class': 'form-control mr-2'}),
        }

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome', 'email', 'fone', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome'}),
            'email': forms.TextInput(attrs={'placeholder': 'Digite o email'}),
            'fone': forms.TextInput(attrs={'placeholder': 'XXXXX-XXXX'}),
            'ativo': forms.Select(choices=Editora.ATIVO_CHOICES, attrs={'class': 'form-control mr-2'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['tipo']
        widgets = {
            'tipo': forms.TextInput(attrs={'placeholder': 'Digite a categoria'})
        }

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['aluno', 'livro']  # Campos que o usuário irá preencher no formulário (o resto é calculado automaticamente)
        widgets = {
            'aluno': forms.Select(attrs={'class': 'form-control mr-2'}),  # Campo para selecionar o aluno
            'livro': forms.Select(attrs={'class': 'form-control mr-2'}),  # Campo para selecionar o livro
            'ativo': forms.Select(choices=Editora.ATIVO_CHOICES, attrs={'class': 'form-control mr-2'}),

        }