# Generated by Django 5.1.3 on 2024-11-11 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_leitura', '0008_alter_livro_ano_alter_livro_vol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='ano',
            field=models.PositiveIntegerField(),
        ),
    ]
