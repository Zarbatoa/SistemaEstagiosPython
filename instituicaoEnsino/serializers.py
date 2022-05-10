from rest_framework import serializers
from instituicaoEnsino.models import InstituicaoEnsino
from endereco.serializers import EnderecoSerializer

class InstituicaoEnsinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituicaoEnsino
        fields = ('__all__')

class InstituicaoEnsinoGetSerializer(serializers.ModelSerializer):
    
    endereco = EnderecoSerializer()
    class Meta:
        model = InstituicaoEnsino
        fields = ('__all__')