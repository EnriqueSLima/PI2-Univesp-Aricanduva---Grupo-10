# Generated by Django 5.1.3 on 2024-11-08 22:46

import django.db.models.deletion
import django.utils.timezone
import sala_leitura.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('ra', models.CharField(max_length=20, unique=True)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=50)),
                ('fone', models.PositiveIntegerField()),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tombo', models.DateField()),
                ('registro', models.IntegerField(unique=True)),
                ('autor', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200)),
                ('procedencia', models.CharField(max_length=200)),
                ('exemplar', models.PositiveIntegerField()),
                ('colecao', models.CharField(max_length=200)),
                ('edicao', models.CharField(max_length=50)),
                ('ano', models.PositiveIntegerField()),
                ('vol', models.PositiveIntegerField()),
                ('editora', models.CharField(max_length=200)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('aquisicao', models.CharField(choices=[('C', 'Compra'), ('D', 'Doação'), ('T', 'Troca')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_emprestimo', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_devolucao', models.DateTimeField(default=sala_leitura.models.data_devolucao_default)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sala_leitura.aluno')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sala_leitura.livro')),
            ],
        ),
    ]
