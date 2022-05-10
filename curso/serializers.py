from rest_framework import serializers
from curso.models import Curso
from instituicaoEnsino.serializers import InstituicaoEnsinoGetSerializer

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('__all__')

class CursoGetSerializer(serializers.ModelSerializer):
    
    instituicaoEnsino = InstituicaoEnsinoGetSerializer()
    class Meta:
        model = Curso
        fields = ('__all__')