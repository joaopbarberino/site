# Generated by Django 2.1.7 on 2019-03-17 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0004_auto_20190317_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.CharField(default='SOBRENOME, Nome (Apenas o 1º)', max_length=120, verbose_name='Nome do autor'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.CharField(choices=[('as', 'Artes'), ('ba', 'Biologia'), ('cs', 'Ciências'), ('el', 'Espanhol'), ('fi', 'Filosofia'), ('fa', 'Física'), ('ga', 'Geografia'), ('ha', 'História'), ('ia', 'Informática'), ('is', 'Inglês'), ('ma', 'Matemática'), ('ps', 'Português'), ('qa', 'Química'), ('sa', 'Sociologia')], max_length=2, verbose_name='Gênero'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='nome',
            field=models.CharField(max_length=120, verbose_name='Nome do Livro'),
        ),
    ]
