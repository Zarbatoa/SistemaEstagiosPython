from rest_framework.viewsets import ModelViewSet
from unidadeConcedente.models import UnidadeConcedente
from unidadeConcedente.serializers import UnidadeConcedenteGetSerializer, UnidadeConcedente, UnidadeConcedenteSerializer

class UnidadeConcedenteViewSet(ModelViewSet):

    queryset = UnidadeConcedente.objects.all()
    serializer_class = UnidadeConcedenteSerializer
    http_method_names = ['get', 'post', 'patch']

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = UnidadeConcedenteGetSerializer
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.serializer_class = UnidadeConcedenteGetSerializer
        return super().list(request, *args, **kwargs)

