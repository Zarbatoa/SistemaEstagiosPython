from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator
from endereco.models import Endereco

class InstituicaoEnsino(models.Model):
    
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

    representante = models.CharField(
        max_length=255
    )

    telefone_fixo = models.CharField(
        max_length=25,
    )
    
    telefone_cel = models.CharField(
        max_length=25,
        null=True
    )

    info_relevante = models.CharField(
        max_length=255,
        null=True
    )

    endereco = models.ForeignKey(Endereco, models.DO_NOTHING, null=True, default=None, related_name="instituicao_endereco")
