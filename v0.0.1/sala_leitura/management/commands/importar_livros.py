import csv
from django.core.management.base import BaseCommand
from sala_leitura.models import Livro
from datetime import datetime

class Command(BaseCommand):
    help = 'Importa dados de livros a partir de um arquivo CSV'

    def handle(self, *args, **kwargs):
        with open('livros_emef.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Extraindo os dados do CSV
                tombo = row['Tombo'].strip() if row['Tombo'].strip() else None  # Verificar se 'Tombo' não está vazio
                registro = int(row['Registro'].strip())  
                autor = row['Autor'].strip()
                titulo = row['Título'].strip()
                procedencia = row['Procedencia'].strip()
                exemplar = row['Exemplar'].strip()
                
                # Verificando se o campo 'Exemplar' está vazio
                exemplar = row['Exemplar'].strip()  # Pegando o valor de 'Exemplar'
                if exemplar:  # Se 'Exemplar' não for vazio
                    try:
                        exemplar = int(exemplar)  # Tenta converter para inteiro
                    except ValueError:
                        self.stdout.write(self.style.ERROR(f'Valor inválido para o campo "Exemplar" no livro "{titulo}". Ignorando este livro.'))
                        continue  # Ignora o livro se o valor não puder ser convertido
                else:
                    exemplar = 0    # Ou um valor padrão, como 0 conforme necessário
                colecao = row['Coleção'].strip()
                edicao = row['Edição'].strip()

                # Verificando se o campo 'Ano' está vazio
                ano_str = row['Ano'].strip()  # Pegando o valor de 'Ano'
                if ano_str:  # Se 'Ano' não for vazio
                    try:
                        ano = int(ano_str)  # Tenta converter para inteiro
                    except ValueError:
                        self.stdout.write(self.style.ERROR(f'Valor inválido para o campo "Ano" no livro "{titulo}". Ignorando este livro.'))
                        continue  # Ignora o livro se o valor não puder ser convertido
                else:
                    ano = None  # Ou um valor padrão, como 0 ou 2020, conforme necessário

                vol = row['Volume'].strip()  
                editora = row['Editora'].strip()
                categoria = row.get('Categorias', '').strip()  
                aquisicao = row['aquisicao'].strip()  

                # Verificando se 'vol' é um número válido
                if vol.isdigit():  
                    vol = int(vol)
                else:
                    vol = None  # Substitua por um valor padrão, caso necessário

                # Convertendo o 'tombo' para o formato correto, apenas se não for None
                if tombo:
                    try:
                        tombo = datetime.strptime(tombo, '%Y-%m-%d')  # Se 'tombo' não for vazio, converte para datetime
                    except ValueError:
                        self.stdout.write(self.style.ERROR(f'Erro ao processar o tombo para o livro "{titulo}". Valor: "{tombo}"'))
                        tombo = datetime(2000, 1, 1)  # Atribui uma data padrão válida
                else:
                    tombo = datetime(2000, 1, 1)  # Atribui uma data padrão válida caso 'tombo' esteja vazio

                # Verifica se a aquisição é válida
                if aquisicao not in dict(Livro.AQUISICAO_CHOICES).keys():
                    self.stdout.write(self.style.ERROR(f'Aquisição inválida para o livro "{titulo}". Ignorando o livro.'))
                    continue

                # Verificando se o livro já existe pelo 'registro'
                if Livro.objects.filter(registro=registro).exists():
                    self.stdout.write(self.style.WARNING(f'O livro com registro "{registro}" já existe. Ignorando este livro.'))
                    continue  # Ignora o livro se já existir no banco de dados

                # Criando o livro no banco de dados
                Livro.objects.create(
                    tombo=tombo,
                    registro=registro,
                    autor=autor,
                    titulo=titulo,
                    procedencia=procedencia,
                    exemplar=exemplar,
                    colecao=colecao,
                    edicao=edicao,
                    ano=ano,
                    vol=vol,
                    editora=editora,
                    categoria=categoria,
                    aquisicao=aquisicao
                )

        self.stdout.write(self.style.SUCCESS('Dados de livros importados com sucesso!'))

