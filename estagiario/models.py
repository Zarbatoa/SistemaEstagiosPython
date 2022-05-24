from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator

from curso.models import Curso
from endereco.models import Endereco

class Estagiario(models.Model):

    nome = models.CharField(
        max_length=255
    )

    email = models.CharField(
        max_length=255,
        validators=[EmailValidator()]
    )

    data_nascimento = models.DateField(
    )

    cpf = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(14)]
    )

    telefone_fixo = models.CharField(
        max_length=25,
    )
    
    telefone_cel = models.CharField(
        max_length=25,
        null=True
    )

    nome_do_pai = models.CharField(
        max_length=255
    )

    nome_da_mae = models.CharField(
        max_length=255
    )

    matriculado = models.BooleanField(
        default=True
    )

    numero_matricula = models.CharField(
        max_length=255,
        null=True
    )

    representante_legal = models.CharField(
        max_length=255,
        null=True
    )

    rg_rep_legal = models.CharField(
        max_length=45,
        null=True
    )

    endereco = models.ForeignKey(Endereco, models.DO_NOTHING, null=True, default=None, related_name="estagiario_endereco")

    curso = models.ForeignKey(Curso, models.DO_NOTHING, null=True, default=None, related_name="estagiario_curso")

