from django.core.management.base import BaseCommand
import csv
from sala_leitura.models import Editora

class Command(BaseCommand):
    help = 'Importa dados de editoras a partir de um arquivo CSV'

    def handle(self, *args, **kwargs):
        with open('editoras.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                nome = row['Editora'].strip()  # Remove espaços em branco, caso existam
                if nome:  # Verifica se o nome não está vazio
                    Editora.objects.create(nome=nome)

        self.stdout.write(self.style.SUCCESS('Dados de editoras importados com sucesso!'))