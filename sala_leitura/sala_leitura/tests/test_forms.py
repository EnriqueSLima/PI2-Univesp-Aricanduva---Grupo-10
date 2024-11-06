from django.test import TestCase
#from .forms import EditoraForm, LocacaoForm, LocacaoItensForm, ClienteForm, ProdutosForm, TipoProdutoForm, UsuariosForm
from ..forms import EditoraForm, LocacaoForm, LocacaoItensForm, ClienteForm, ProdutosForm, TipoProdutoForm, UsuariosForm

class EditoraFormTest(TestCase):
    def test_formulario_valido(self):
        form_data = {
            'nome': 'Editora Teste',
            'uf': 'SP',
            'contato': 'Contato Teste',
            'ddd': '11',
            'telefone': '1234567890',
            'celular': '11987654321',
            'email': 'teste@example.com',
            'obs': 'Observação Teste',
            'id_usuario': 1,
            'ult_alteracao': '2023-01-01T10:00',
            'ativo': True
        }
        form = EditoraForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_formulario_invalido_telefone(self):
        form_data = {
            'nome': 'Editora Teste',
            'telefone': '12345'  # Telefone inválido
        }
        form = EditoraForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('telefone', form.errors)

class LocacaoFormTest(TestCase):
    def test_formulario_valido(self):
        form_data = {
            'id_cliente': 1,
            'emissao': '2023-01-01T10:00',
            'status': 'Aberto',
            'total': 100.00,
            'observacao': 'Observação Teste',
            'id_usuario': 1,
            'reserva': True,
            'confirma': False,
            'liquida': False
        }
        form = LocacaoForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_formulario_invalido_total_negativo(self):
        form_data = {
            'id_cliente': 1,
            'emissao': '2023-01-01T10:00',
            'status': 'Aberto',
            'total': -100.00,  # Total negativo
            'observacao': 'Observação Teste',
            'reserva': True,
            'confirma': False,
            'liquida': False
        }
        form = LocacaoForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertIn('total', form.errors)

class LocacaoItensFormTest(TestCase):
    def test_formulario_valido(self):
        form_data = {
            'id_locacao': 1,
            'id_produto': 1,
            'titulo': 'Produto Teste',
            'quantidade': 5,
            'dev_prevista_ori': '2023-01-01T10:00',
            'renovou': False,
            'dev_prevista': '2023-01-02T10:00',
            'dev_realizada': '2023-01-03T10:00',
            'devolvido': False,
            'id_usuario': 1
        }
        form = LocacaoItensForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_formulario_invalido_quantidade(self):
        form_data = {
            'quantidade': 1  # Quantidade inválida
        }
        form = LocacaoItensForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertIn('quantidade', form.errors)

class ClienteFormTest(TestCase):
    def test_formulario_valido(self):
        form_data = {
            'nome': 'Cliente Teste',
            'cpf': '123.456.789-00',
            'email': 'cliente@example.com',
            # Adicione outros campos necessários
        }
        form = ClienteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_formulario_invalido_cpf(self):
        form_data = {
            'nome': 'Cliente Teste1',
            'cpf': '123.456.789-11',
            'email': 'cliente@example.com',
            #'cpf': '123.456.789-11'  # CPF inválido
        }
        form = ClienteForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertIn('cpf', form.errors)

class ProdutosFormTest(TestCase):
    def test_formulario_valido(self):
        form_data = {
            'tombo': '2023-01-01T10:00',
            'estoque': 10,
            'titulo': 'Produto Teste',
            'id_usuario': 1,
            # Adicione outros campos necessários
        }
        form = ProdutosForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_formulario_invalido_estoque(self):
        form_data = {
            'estoque': -1  # Estoque negativo
        }
        form = ProdutosForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('estoque', form.errors)

class TipoProdutoFormTest(TestCase):
    def test_formulario_valido(self):
        form_data = {
            'descricao': 'Tipo Teste',
            'ativo': True
        }
        form = TipoProdutoForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

class UsuariosFormTest(TestCase):
    def test_formulario_valido(self):
        form_data = {
            'nome': 'Usuário Teste',
            'senha': 'senha123',
            'id_unidade': 1,
            'id_acesso': 1,
            'ativo': True,
            'obs': 'Observação Teste'
        }
        form = UsuariosForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_formulario_invalido_senha(self):
        form_data = {
            'senha': '123'  # Senha muito curta
        }
        form = UsuariosForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertIn('senha', form.errors)
