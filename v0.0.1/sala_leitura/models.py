from django.db import models
from django.utils import timezone
from datetime import timedelta

class Aluno(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    
    id = models.AutoField(primary_key=True)  # Campo id auto incrementável
    nome = models.CharField(max_length=255)  # Nome do aluno
    ra = models.CharField(max_length=20, unique=True)  # RA do aluno, único
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)  # Sexo do aluno
    ativo = models.BooleanField(default=True)  # Status do aluno (ativo ou não)
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    AQUISICAO_CHOICES = [
        ('C', 'Compra'),
        ('D', 'Doação'),
        ('T', 'Troca'),
    ]
    
    id = models.AutoField(primary_key=True)  # ID automático
    tombo = models.DateField()  # Tombo como data (sem horas e minutos)
    registro = models.IntegerField(unique=True)  # Registro como número inteiro
    autor = models.CharField(max_length=200)  # Autor do livro
    titulo = models.CharField(max_length=200)  # Título do livro
    procedencia = models.CharField(max_length=200)  # Procedência do livro
    exemplar = models.PositiveIntegerField()  # Número do exemplar
    colecao = models.CharField(max_length=200)  # Coleção do livro
    edicao = models.CharField(max_length=50)  # Edição do livro
    ano = models.PositiveIntegerField()  # Ano de publicação
    vol = models.PositiveIntegerField()  # Volume
    editora = models.CharField(max_length=200)  # Editora do livro
    observacao = models.TextField(null=True, blank=True)  # Observações
    aquisicao = models.CharField(max_length=1, choices=AQUISICAO_CHOICES)  # Tipo de aquisição
    
    def __str__(self):
        return f'{self.titulo} ({self.autor})'

class Editora(models.Model):
    id = models.AutoField(primary_key=True)  # ID automático
    nome = models.CharField(max_length=255)  # Nome do aluno
    email = models.CharField(max_length=50)
    fone = models.PositiveIntegerField()
    ativo = models.BooleanField(default=True)  # Status do aluno (ativo ou não)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)  # ID automático
    tipo = models.CharField(max_length=255)  # Nome do aluno

    def __str__(self):
        return self.tipo

class Emprestimo(models.Model):
    id = models.AutoField(primary_key=True)  # ID automático
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)  # Relacionamento com o modelo Aluno
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)  # Relacionamento com o modelo Livro
    data_emprestimo = models.DateTimeField(default=timezone.now)  # Data do empréstimo
    data_devolucao = models.DateTimeField(default=lambda: timezone.now() + timedelta(days=7))  # Data de devolução (7 dias após)

    def __str__(self):
        return f'{self.aluno.nome} - {self.livro.titulo}'