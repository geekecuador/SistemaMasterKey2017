"""Sistema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from material.frontend import urls as frontend_urls
from rest_framework import serializers, viewsets,routers

from masterkey import views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(frontend_urls)),

    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^$', views.login_view, name='index'),
    url(r'^tablero', views.tablero, name='tablero'),
    url(r'^salir/', auth_views.logout, name='salirsistema'),
    url(r'^paso1/', views.paso1, name='paso1'),
    url(r'^paso2/', views.paso2, name='paso2'),
    url(r'^paso3/', views.paso3, name='paso3'),
    url(r'^registro/', views.registro, name='registro'),
    url(r'^academic-rank/', views.academic_rank, name='academic_rank'),
    url(r'^talleres/', views.talleres, name='talleres'),
    url(r'^test/', views.test, name='test'),
    url(r'^ver-talleres/', views.ver_talleres, name='ver-talleres'),
    url(r'^ver-lecciones/', views.ver_lecciones, name='ver-lecciones'),

    url(r'^exportar/estudiantes/$', views.ExportarEstudiantes.as_view(), name='exportarEstudiantes'),
    url(r'^exportar/horarios/$', views.ExportarHorarios.as_view(), name='exportarHorarios'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/', include(router.urls)),
    url(r'^login-android/' , views.login_android, name='login-android')
]
