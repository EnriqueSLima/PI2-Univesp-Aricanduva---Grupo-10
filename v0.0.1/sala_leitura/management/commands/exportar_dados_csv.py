import csv
from django.core.management.base import BaseCommand
from sala_leitura.models import Produtos  # Substitua pelo nome do seu modelo

class Command(BaseCommand):
    help = 'Exporta dados do modelo Produto para um arquivo CSV'

    def handle(self, *args, **kwargs):
        # Nome do arquivo CSV de saída
        nome_do_arquivo = 'produtos_exportados.csv'
        
        # Obtenha todos os registros do modelo
        produtos = Produtos.objects.all()

        # Abra o arquivo CSV para escrita
        with open(nome_do_arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Escreva o cabeçalho (colunas)
            writer.writerow(['id_produto', 'tombo', 'numero_tombo', 'codigo_de_barras', 
                            'autor', 'titulo', 'procedencia' ,'estoque', 'local_estoque',
                            'id_editora', 'colecao', 'edicao', 'volume', 'ano', 'id_tipo_produto', 
                            'defeito', 'bloquear', 'aquisicao_c', 'aquisicao_d', 'aquisicao_t', 
                            'id_usuario', 'ult_alteracao', 'obs', 'data_cadastro' ])  # Ajuste conforme os campos do modelo

            # Escreva os dados de cada registro
            for produto in produtos:
                writer.writerow([produto.id_produto, produto.tombo, produto.numero_tombo, produto.codigo_de_barras, 
                            produto.autor, produto.titulo, produto.procedencia ,produto.estoque, produto.local_estoque,
                            produto.id_editora, produto.colecao, produto.edicao, produto.volume, produto.ano, produto.id_tipo_produto, 
                            produto.defeito, produto.bloquear, produto.aquisicao_c, produto.aquisicao_d, produto.aquisicao_t, 
                            produto.id_usuario, produto.ult_alteracao, produto.obs, produto.data_cadastro])  # Ajuste conforme os campos

        self.stdout.write(self.style.SUCCESS(f'Dados exportados com sucesso para {nome_do_arquivo}'))
