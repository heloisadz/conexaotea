# Generated by Django 5.0.2 on 2024-07-22 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_alter_biblioteca_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biblioteca',
            name='arquivo',
            field=models.FileField(default='', upload_to='arquivos/'),
        ),
    ]
