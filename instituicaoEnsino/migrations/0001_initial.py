# Generated by Django 4.0.4 on 2022-05-10 13:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('endereco', '0002_alter_endereco_cep'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstituicaoEnsino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=17, validators=[django.core.validators.MinLengthValidator(16)])),
                ('email', models.CharField(max_length=255, validators=[django.core.validators.EmailValidator()])),
                ('representante', models.CharField(max_length=255)),
                ('telefone_fixo', models.CharField(max_length=25)),
                ('telefone_cel', models.CharField(max_length=25, null=True)),
                ('info_relevante', models.CharField(max_length=255)),
                ('endereco', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='instituicao_endereco', to='endereco.endereco')),
            ],
        ),
    ]