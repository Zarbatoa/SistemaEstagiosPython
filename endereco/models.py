from secrets import choice
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator

class Ufs(models.TextChoices):
    SC = 'SC', _('Santa Catarina')
    RS = 'RS', _('Rio Grande do Sul')
    PR = 'PR', _('Paraná')
    SP = 'SP', _('São Paulo')
    RJ = 'RJ', _('Rio de Janeiro')

class Endereco(models.Model):
    logradouro = models.CharField(
        max_length=50
    )

    numero = models.CharField(
        max_length=5
    )

    complemento = models.CharField(
        max_length=50,
        null=True,
    )

    bairro = models.CharField(
        max_length=50
    )

    cep = models.CharField(
        max_length=9,
        validators=[MinLengthValidator(8)]
    )

    cidade = models.CharField(
        max_length=50
    )

    uf = models.CharField(
        max_length=2,
        choices=Ufs.choices
    )