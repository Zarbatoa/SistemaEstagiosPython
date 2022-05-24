from rest_framework.viewsets import ModelViewSet
from estagio.models import Estagio
from estagio.serializers import EstagioGetSerializer, EstagioSerializer

class EstagioViewSet(ModelViewSet):

    queryset = Estagio.objects.all()
    serializer_class = EstagioSerializer
    http_method_names = ['get', 'post', 'patch']

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = EstagioGetSerializer
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.serializer_class = EstagioGetSerializer
        return super().list(request, *args, **kwargs)

