from rest_framework.viewsets import ModelViewSet
from unidadeConcedente.models import UnidadeConcedente
from unidadeConcedente.serializers import UnidadeConcedenteGetSerializer, UnidadeConcedenteSerializer

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication 

class UnidadeConcedenteViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)# DjangoModelPermissions)
    authentication_classes = (TokenAuthentication,)

    queryset = UnidadeConcedente.objects.all()
    serializer_class = UnidadeConcedenteSerializer
    http_method_names = ['get', 'post', 'patch']

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = UnidadeConcedenteGetSerializer
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.serializer_class = UnidadeConcedenteGetSerializer
        return super().list(request, *args, **kwargs)

