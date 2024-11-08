import pytz
from django.test import TestCase
from django.urls import reverse
from ..models import Editora, Locacao, LocacaoItens, Cliente, Produtos, TipoProduto, Usuarios

class EditoraViewTest(TestCase):

    def setUp(self):
        timezone.activate(pytz.timezone('America/Sao_Paulo'))  # Ative o fuso horário desejado
        self.editora = Editora.objects.create(
            nome="Editora Teste",
            uf="SP",
            contato="Contato Teste",
            ddd="11",
            telefone="123456789",
            celular="987654321",
            email="teste@editora.com",
            obs="Observação Teste",
            id_usuario=1,
            ult_alteracao="2023-10-27T12:00:00",
            ativo=True
        )

    def test_editora_view_status_code(self):
        response = self.client.get(reverse('cadastrar_editora', args=[self.editora.id]))
        self.assertEqual(response.status_code, 200)

    def test_editora_view_template_used(self):
        response = self.client.get(reverse('cadastrar_editora', args=[self.editora.id]))
        self.assertTemplateUsed(response, 'cadastrar_editora.html')

class LocacaoViewTest(TestCase):

    def setUp(self):
        timezone.activate(pytz.timezone('America/Sao_Paulo'))  # Ative o fuso horário desejado
        self.locacao = Locacao.objects.create(
            id_cliente=1,
            emissao="2023-10-27T12:00:00",
            status="Ativo",
            total=100.00,
            observacao="Observação Teste",
            id_usuario=1,
            reserva=False,
            confirma=False,
            liquida=False
        )

    def test_locacao_view_status_code(self):
        response = self.client.get(reverse('cadastrar_locacao', args=[self.locacao.id]))
        self.assertEqual(response.status_code, 200)

    def test_locacao_view_template_used(self):
        response = self.client.get(reverse('cadastrar_locacao', args=[self.locacao.id]))
        self.assertTemplateUsed(response, 'cadastrar_locacao.html')

class ClienteViewTest(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome="Cliente Teste",
            nome_social="Nome Social Teste",
            tipo="Tipo Teste",
            cpf="000.000.000-00",
            ie_rg="RG Teste",
            endereco="Endereço Teste",
            numero="123",
            cep="00000-000",
            bairro="Bairro Teste",
            cidade="Cidade Teste",
            estado="Estado Teste",
            uf="SP",
            contato="Contato Teste",
            ddd="11",
            telefone="123456789",
            celular="987654321",
            email="cliente@teste.com",
            obs="Observação Teste",
            ativo=True
        )

    def test_cliente_view_status_code(self):
        response = self.client.get(reverse('cadastrar_cliente', args=[self.cliente.id]))
        self.assertEqual(response.status_code, 200)

    def test_cliente_view_template_used(self):
        response = self.client.get(reverse('cadastrar_cliente', args=[self.cliente.id]))
        self.assertTemplateUsed(response, 'cadastrar_cliente.html')

