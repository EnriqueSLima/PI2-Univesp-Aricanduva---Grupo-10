# Generated by Django 5.1.3 on 2024-11-11 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala_leitura', '0006_alter_editora_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='categoria',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
