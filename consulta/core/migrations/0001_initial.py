# Generated by Django 3.1.6 on 2021-02-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CursoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, verbose_name='nome')),
                ('num_vagas', models.IntegerField(verbose_name='Número de vagas')),
            ],
        ),
    ]
