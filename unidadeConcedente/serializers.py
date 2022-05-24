from rest_framework import serializers
from unidadeConcedente.models import UnidadeConcedente

from endereco.serializers import EnderecoSerializer

class UnidadeConcedenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeConcedente
        fields = ('__all__')

class UnidadeConcedenteGetSerializer(serializers.ModelSerializer):
    
    endereco = EnderecoSerializer()

    class Meta:
        model = UnidadeConcedente
        fields = ('__all__')