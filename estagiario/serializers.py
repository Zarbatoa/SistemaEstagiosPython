from rest_framework import serializers
from estagiario.models import Estagiario

from endereco.serializers import EnderecoSerializer
from curso.serializers import CursoGetSerializer

class EstagiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estagiario
        fields = ('__all__')

class EstagiarioGetSerializer(serializers.ModelSerializer):
    
    endereco = EnderecoSerializer()
    curso = CursoGetSerializer()

    class Meta:
        model = Estagiario
        fields = ('__all__')