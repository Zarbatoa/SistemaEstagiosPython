from rest_framework import serializers
from django.contrib.auth.models import AbstractUser

from usuario.models import UsuarioModel

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = ('__all__')