from rest_framework import serializers
from estagio.models import Estagio

from estagiario.serializers import EstagiarioGetSerializer
from unidadeConcedente.serializers import UnidadeConcedenteGetSerializer

class EstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estagio
        fields = ('__all__')

class EstagioGetSerializer(serializers.ModelSerializer):
    
    estagiario = EstagiarioGetSerializer()
    unidadeConcedente = UnidadeConcedenteGetSerializer()

    class Meta:
        model = Estagio
        fields = ('__all__')