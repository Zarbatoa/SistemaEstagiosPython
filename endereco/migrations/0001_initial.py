# Generated by Django 4.0.3 on 2022-05-26 13:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=5)),
                ('complemento', models.CharField(max_length=50, null=True)),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(8)])),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(choices=[('SC', 'Santa Catarina'), ('RS', 'Rio Grande do Sul'), ('PR', 'Paraná'), ('SP', 'São Paulo'), ('RJ', 'Rio de Janeiro')], max_length=2)),
            ],
        ),
    ]
