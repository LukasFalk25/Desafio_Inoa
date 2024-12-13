# Generated by Django 5.1.4 on 2024-12-13 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('codigo', models.CharField(max_length=14, unique=True)),
                ('limite_inferior', models.FloatField()),
                ('limite_superior', models.FloatField()),
                ('periodicidade', models.IntegerField(help_text='Periodicidade em minutos')),
            ],
        ),
    ]
