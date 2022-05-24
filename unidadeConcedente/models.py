from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator

from endereco.models import Endereco

class UnidadeConcedente(models.Model):
    
    razao_social = models.CharField(
        max_length=255
    )

    cnpj = models.CharField(
        max_length=18,
        validators=[MinLengthValidator(17)]
    )

    email = models.CharField(
        max_length=255,
        validators=[EmailValidator()]
    )

    telefone_fixo = models.CharField(
        max_length=25,
    )
    
    telefone_cel = models.CharField(
        max_length=25,
        null=True
    )

    representante = models.CharField(
        max_length=255
    )

    cargo_representante = models.CharField(
        max_length=255
    )

    cpf_representante = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(14)]
    )

    info_relevantes = models.CharField(
        max_length=255,
        null=True
    )

    eh_agencia_integradora = models.BooleanField(
        default=False
    )

    endereco = models.ForeignKey(Endereco, models.DO_NOTHING, null=True, default=None, related_name="unidade_concedente_endereco")
