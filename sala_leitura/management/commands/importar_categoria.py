from django.core.management.base import BaseCommand
import csv
from sala_leitura.models import Categoria

class Command(BaseCommand):
    help = 'Importa dados de categorias a partir de um arquivo CSV'

    def handle(self, *args, **kwargs):
        with open('categorias.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                tipo = row['Categoria']
                Categoria.objects.create(tipo=tipo)
        
        self.stdout.write(self.style.SUCCESS('Dados de Categorias importados com sucesso!'))





