# from django.shortcuts import render
import re
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication 

from curso.models import Curso
from curso.serializers import CursoGetSerializer, CursoSerializer

class CursoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)# DjangoModelPermissions)
    authentication_classes = (TokenAuthentication,)

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    http_method_names = ['get', 'post', 'patch']

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CursoGetSerializer
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.serializer_class = CursoGetSerializer
        return super().list(request, *args, **kwargs)

