import csv
from django.core.management.base import BaseCommand
from sala_leitura.models import Cliente  # Substitua pelo nome do seu app e modelo

class Command(BaseCommand):
    help = 'Importa dados do arquivo CSV para o modelo Cliente'

    def add_arguments(self, parser):
        # Permite especificar o caminho do arquivo CSV como argumento
        parser.add_argument('caminho_csv', type=str, help='O caminho do arquivo CSV a ser importado')

    def handle(self, *args, **options):
        caminho_csv = options['caminho_csv']
        
        try:
            with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    Cliente.objects.create(
                        id_cliente=row.get('id_cliente'),
                        nome=row.get('nome'),
                        nome_social=row.get('nome_social'),
                        tipo=row.get('tipo'),
                        cpf=row.get('cpf'),
                        ie_rg=row.get('ie_rg'),
                        endereco=row.get('endereco'),
                        numero=row.get('numero'),
                        cep=row.get('cep'),
                        bairro=row.get('bairro'),
                        cidade=row.get('cidade'),
                        estado=row.get('estado'),
                        uf=row.get('uf'),
                        contato=row.get('contato'),
                        ddd=row.get('ddd'),
                        telefone=row.get('telefone'),
                        celular=row.get('celular'),
                        email=row.get('email'),
                        obs=row.get('obs'),
                        ativo=row.get('ativo') == 'True',  # Converter para booleano
                        ra=row.get('ra'),
                        sexo=row.get('sexo')
                    )

            self.stdout.write(self.style.SUCCESS(f'Dados importados com sucesso de {caminho_csv}'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Arquivo {caminho_csv} não encontrado'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao importar dados: {e}'))
