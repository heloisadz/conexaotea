# Generated by Django 5.0.2 on 2024-07-22 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_alter_biblioteca_arquivo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biblioteca',
            old_name='arquivo',
            new_name='arquivos',
        ),
    ]
