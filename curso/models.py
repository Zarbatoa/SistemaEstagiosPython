from secrets import choice
from django.db import models
from django.utils.translation import gettext_lazy as _
from instituicaoEnsino.models import InstituicaoEnsino

class Turnos(models.TextChoices):
    MAT = 'MAT', _('Matutino')
    VES = 'VES', _('Vespertino')
    NOT = 'NOT', _('Noturno')

class Curso(models.Model):

    nome = models.CharField(
        max_length=255
    )

    turno = models.CharField(
        max_length=3,
        choices=Turnos.choices
    )

    modalidade = models.CharField(
        max_length=255
    )

    instituicaoEnsino = models.ForeignKey(InstituicaoEnsino, models.DO_NOTHING, null=True, default=None, related_name="curso_instituicao")
