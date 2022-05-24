from rest_framework.viewsets import ModelViewSet
from estagiario.models import Estagiario
from estagiario.serializers import EstagiarioGetSerializer, EstagiarioSerializer

class EstagiarioViewSet(ModelViewSet):

    queryset = Estagiario.objects.all()
    serializer_class = EstagiarioSerializer
    http_method_names = ['get', 'post', 'patch']

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = EstagiarioGetSerializer
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.serializer_class = EstagiarioGetSerializer
        return super().list(request, *args, **kwargs)

