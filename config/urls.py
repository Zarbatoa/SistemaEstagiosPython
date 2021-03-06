"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from endereco.views import EnderecoViewSet
from estagiario.views import EstagiarioViewSet
from estagio.views import EstagioViewSet
from instituicaoEnsino.views import InstituicaoEnsinoViewSet
from curso.views import CursoViewSet
from unidadeConcedente.views import UnidadeConcedenteViewSet
from usuario.views import UsuarioAuthView, UsuarioViewSet


router =  routers.SimpleRouter()

router.register('endereco', EnderecoViewSet)
router.register('instituicaoEnsino', InstituicaoEnsinoViewSet)
router.register('curso', CursoViewSet)
router.register('estagiario', EstagiarioViewSet)
router.register('unidadeConcedente', UnidadeConcedenteViewSet)
router.register('estagio', EstagioViewSet)

router.register("usuario", UsuarioViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/token/', UsuarioAuthView.as_view()),
]
