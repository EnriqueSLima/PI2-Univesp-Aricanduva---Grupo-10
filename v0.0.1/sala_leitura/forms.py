from django import forms
from .models import TipoProduto, Usuarios, Produtos, Cliente, Editora, Locacao, LocacaoItens


class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = [
            'nome', 'uf', 'contato', 'ddd', 'telefone', 'celular', 'email', 'obs', 
            'id_usuario', 'ult_alteracao', 'ativo'
        ]
        widgets = {
            'ult_alteracao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(XX) XXXX-XXXX'}),
            'celular': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'}),
            'email': forms.EmailInput(),
        }

    # Validações adicionais, se necessário
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone and len(telefone) < 10:
            raise forms.ValidationError("O telefone deve ter pelo menos 10 dígitos.")
        return telefone

class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = [
            'id_cliente', 'emissao', 'status', 'total', 'observacao', 'id_usuario',
            'reserva', 'confirma', 'liquida'
        ]
        widgets = {
            'emissao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'observacao': forms.Textarea(attrs={'rows': 3}),
        }

    # Validações adicionais, se necessário
    def clean_total(self):
        total = self.cleaned_data.get('total')
        if total is not None and total < 0:
            raise forms.ValidationError("O valor total não pode ser negativo.")
        return total

class LocacaoItensForm(forms.ModelForm):
    class Meta:
        model = LocacaoItens
        fields = [
            'id_locacao', 'id_produto', 'titulo', 'quantidade', 'dev_prevista_ori', 
            'renovou', 'dev_prevista', 'dev_realizada', 'devolvido', 'id_usuario'
        ]
        widgets = {
            'dev_prevista_ori': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'dev_prevista': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'dev_realizada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    # Validações adicionais, se necessário
    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        if quantidade is not None and quantidade <= 0:
            raise forms.ValidationError("A quantidade deve ser maior que zero.")
        return quantidade


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome', 'nome_social', 'tipo', 'cpf', 'ie_rg', 'endereco', 'numero', 'cep', 
            'bairro', 'cidade', 'estado', 'uf', 'contato', 'ddd', 'telefone', 'celular', 
            'email', 'obs', 'ativo'
        ]
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),
            'cep': forms.TextInput(attrs={'placeholder': '00000-000'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(XX) XXXX-XXXX'}),
            'celular': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'}),
            'email': forms.EmailInput(),
        }

    # Validações adicionais, se necessário
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf and len(cpf) != 14:
            raise forms.ValidationError("O CPF deve estar no formato 000.000.000-00.")
        return cpf

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = [
            'tombo', 'numero_tombo', 'codigo_de_barras', 'autor', 'titulo', 'procedencia',
            'estoque', 'local_estoque', 'id_editora', 'colecao', 'edicao', 'volume', 'ano',
            'id_tipo_produto', 'defeito', 'bloquear', 'aquisicao_c', 'aquisicao_d', 'aquisicao_t',
            'id_usuario', 'ult_alteracao', 'obs', 'data_cadastro', 'capa'
        ]
        widgets = {
            'tombo': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'ult_alteracao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_cadastro': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'capa': forms.ClearableFileInput(),  # Para uploads de arquivos
        }
    
    # Validações adicionais, se necessário
    def clean_estoque(self):
        estoque = self.cleaned_data.get('estoque')
        if estoque is not None and estoque < 0:
            raise forms.ValidationError("O estoque não pode ser negativo.")
        return estoque

class TipoProdutoForm(forms.ModelForm):
    class Meta:
        model = TipoProduto
        fields = ['descricao', 'ativo']  # Inclua os campos que deseja no formulário

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nome', 'senha', 'id_unidade', 'id_acesso', 'ativo', 'obs']
        widgets = {
            'senha': forms.PasswordInput(),  # Para exibir o campo 'senha' como senha
        }

    # Validações adicionais, se necessário
    def clean_senha(self):
        senha = self.cleaned_data.get('senha')
        if len(senha) < 6:
            raise forms.ValidationError("A senha deve ter pelo menos 6 caracteres.")
        return senha
