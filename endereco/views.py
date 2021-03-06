from rest_framework.viewsets import ModelViewSet

from endereco.models import Endereco
from endereco.serializers import EnderecoSerializer, serializers

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication

class EnderecoViewSet(ModelViewSet):

    permission_classes = (IsAuthenticated,)# DjangoModelPermissions)
    authentication_classes = (TokenAuthentication,)
    
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    http_method_names = ['get', 'post', 'patch']
