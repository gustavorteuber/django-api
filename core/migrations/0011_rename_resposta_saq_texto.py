# Generated by Django 4.1.5 on 2023-01-24 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_saq'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saq',
            old_name='resposta',
            new_name='texto',
        ),
    ]
