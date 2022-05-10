from rest_framework.viewsets import ModelViewSet

from endereco.models import Endereco
from endereco.serializers import EnderecoSerializer, serializers

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    http_method_names = ['get', 'post', 'patch']
