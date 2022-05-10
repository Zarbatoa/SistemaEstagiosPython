# Generated by Django 4.0.4 on 2022-05-10 12:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]
