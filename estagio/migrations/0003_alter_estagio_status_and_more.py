# Generated by Django 4.0.3 on 2022-05-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0002_alter_estagio_carga_horaria_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estagio',
            name='status',
            field=models.CharField(choices=[('ATIVO', 'Estágio Ativo'), ('INATIVO', 'Estágio Inativo'), ('RESCINDIDO', 'Estágio Inativo Rescindido')], default='ATIVO', max_length=10),
        ),
        migrations.AlterField(
            model_name='estagio',
            name='tem_agencia_integradcao',
            field=models.BooleanField(default=False),
        ),
    ]
