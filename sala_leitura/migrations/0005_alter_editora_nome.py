# Generated by Django 5.1.3 on 2024-11-11 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_leitura', '0004_alter_aluno_ativo_alter_editora_ativo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editora',
            name='nome',
            field=models.CharField(max_length=400),
        ),
    ]
