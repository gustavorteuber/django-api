# Generated by Django 4.1.5 on 2023-01-29 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_acoes_curso_dolar_curso_indice_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contatos',
            old_name='instagram',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='contatos',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contatos',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='contatos',
            name='whatsapp',
        ),
        migrations.RemoveField(
            model_name='contatos',
            name='youtube',
        ),
    ]
