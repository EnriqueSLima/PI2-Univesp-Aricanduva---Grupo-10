import csv
from django.core.management.base import BaseCommand
from sala_leitura.models import Cliente  # Substitua pelo nome do seu app

class Command(BaseCommand):
    help = 'Exporta dados do modelo Cliente para um arquivo CSV'

    def handle(self, *args, **kwargs):
        # Nome do arquivo CSV de saída
        nome_do_arquivo = 'clientes_exportados.csv'

        # Obtenha todos os registros do modelo Cliente
        clientes = Cliente.objects.all()

        # Abra o arquivo CSV para escrita
        with open(nome_do_arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Escreva o cabeçalho (colunas) com o nome de cada campo
            writer.writerow([
                'id_cliente', 'nome', 'nome_social', 'tipo', 'cpf', 'ie_rg', 'endereco', 'numero', 'cep', 
                'bairro', 'cidade', 'estado', 'uf', 'contato', 'ddd', 'telefone', 'celular', 'email', 'obs', 
                'ativo', 'ra', 'sexo'
            ])

            # Escreva os dados de cada cliente
            for cliente in clientes:
                writer.writerow([
                    cliente.id_cliente, cliente.nome, cliente.nome_social, cliente.tipo, cliente.cpf, cliente.ie_rg, 
                    cliente.endereco, cliente.numero, cliente.cep, cliente.bairro, cliente.cidade, cliente.estado, 
                    cliente.uf, cliente.contato, cliente.ddd, cliente.telefone, cliente.celular, cliente.email, 
                    cliente.obs, cliente.ativo, cliente.ra, cliente.sexo
                ])

        self.stdout.write(self.style.SUCCESS(f'Dados exportados com sucesso para {nome_do_arquivo}'))
