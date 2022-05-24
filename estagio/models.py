from django.db import models
from django.utils.translation import gettext_lazy as _
from estagiario.models import Estagiario
from unidadeConcedente.models import UnidadeConcedente

class StatusEstagio(models.TextChoices):
    ATIVO = 'ATIVO', _('Estágio Ativo')
    INATIVO = 'INATIVO', _('Estágio Inativo')
    RESCINDIDO = 'RESCINDIDO', _('Estágio Inativo Rescindido')

class Estagio(models.Model):
    
    supervisor = models.CharField(
        max_length=255
    )

    cargo_supervisor = models.CharField(
        max_length=255
    )

    formacao_academica = models.CharField(
        max_length=255,
    )

    tempo_experiencia = models.CharField(
        max_length=255,
    )
    
    professor = models.CharField(
        max_length=255,
    )

    anofase = models.CharField(
        max_length=255
    )

    horario_estagio = models.CharField(
        max_length=255
    )

    jornada_semanal = models.DecimalField(
        decimal_places=2,
        max_digits=6
    )

    carga_horaria_total = models.DecimalField(
        decimal_places=2,
        max_digits=6
    )

    remuneracao = models.DecimalField(
        decimal_places=2,
        max_digits=6
    )

    valor_vale_transporte = models.DecimalField(
        decimal_places=2,
        max_digits=6
    )

    data_inicio = models.DateField(
    )

    data_termino = models.DateField(
    )

    setor_ou_area = models.CharField(
        max_length=255
    )

    municipio = models.CharField(
        max_length=255
    )

    num_apolice_seguro = models.CharField(
        max_length=255,
        null=True
    )

    tipo_estagio = models.CharField(
        max_length=255
    )

    tem_agencia_integradcao = models.BooleanField(
        default=False
    )

    status = models.CharField(
        max_length=10,
        choices=StatusEstagio.choices,
        default=StatusEstagio.ATIVO
    )

    nome_agencia_integracao = models.CharField(
        max_length=255,
        null=True
    )

    rquadrimestral1 = models.BooleanField(
        default=False
    )

    rquadrimestral2 = models.BooleanField(
        default=False
    )

    rquadrimestral3 = models.BooleanField(
        default=False
    )

    rquadrimestral4 = models.BooleanField(
        default=False
    )

    rquadrimestral5 = models.BooleanField(
        default=False
    )

    rquadrimestral6 = models.BooleanField(
        default=False
    )


    estagiario = models.ForeignKey(Estagiario, models.DO_NOTHING, null=True, default=None, related_name="estagio_estagiario")

    unidadeConcedente = models.ForeignKey(UnidadeConcedente, models.DO_NOTHING, null=True, default=None, related_name="estagio_unidade_concedente")
