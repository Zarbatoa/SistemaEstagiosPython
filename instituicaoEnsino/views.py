# from django.shortcuts import render
import re
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication 

from instituicaoEnsino.models import InstituicaoEnsino
from instituicaoEnsino.serializers import InstituicaoEnsinoGetSerializer, InstituicaoEnsinoSerializer

class InstituicaoEnsinoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)# DjangoModelPermissions)
    authentication_classes = (TokenAuthentication,)

    queryset = InstituicaoEnsino.objects.all()
    serializer_class = InstituicaoEnsinoSerializer
    http_method_names = ['get', 'post', 'patch']

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = InstituicaoEnsinoGetSerializer
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.serializer_class = InstituicaoEnsinoGetSerializer
        return super().list(request, *args, **kwargs)

