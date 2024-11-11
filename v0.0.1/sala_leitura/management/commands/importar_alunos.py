from django.core.management.base import BaseCommand
import csv
from sala_leitura.models import Aluno

class Command(BaseCommand):
    help = 'Importa dados de alunos a partir de um arquivo CSV'

    def handle(self, *args, **kwargs):
        with open('alunos_emef.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                nome = row['nome'].strip()
                ra = row['ra'].strip()
                sexo = row['sexo'].strip()

                if nome and ra and sexo:  # Verifica se todos os campos estão preenchidos
                    # Verifica se o RA já existe no banco
                    if not Aluno.objects.filter(ra=ra).exists():
                        Aluno.objects.create(
                            nome=nome,
                            ra=ra,
                            sexo=sexo,
                            ativo=True  # Define o valor do campo 'ativo' como True
                        )
                    else:
                        self.stdout.write(self.style.WARNING(f'O RA {ra} já existe. Não foi inserido.'))

        self.stdout.write(self.style.SUCCESS('Dados de alunos importados com sucesso!'))