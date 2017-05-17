"""controlc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import  include, url
from django.contrib import admin
from configuracion import views
from establecimiento import views as viewEst
from django.conf import settings
from django.conf.urls.static import static

# Autenticacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

app_name = 'micolegio'
# from django.conf.urls import patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),   
    #----------
    # Inicio de sesion
    url(r'^login/$', views.ingresar, name='login'),
    url(r'^auth/$', views.ingresar, name='ingresar'),
    url(r'^accounts/login/$', views.ingresar, name='ingresar'),
    url(r'^cerrar/$', views.cerrar, name='cerrar'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),

    # ---------
    # Parametricas Establecimientos
    url(r'^configuracion/Metodologias/$', views.indexMetodologias),
    url(r'^configuracion/MetodologiasJson/$', views.MetodologiasJson),
    url(r'^configuracion/editarMetodologia/(?P<id>[0-9]+)/$', views.formularioEditarMetodologia),
    url(r'^configuracion/registrarMetodologia/$', views.formularioRegistrarMetodologia),

    # ---------
    # Administracion de Establecimientos
    url(r'^establecimiento/Establecimientos/$', viewEst.indexEstablecimientos),
    url(r'^establecimiento/EstablecimientosJson/$', viewEst.EstablecimientosJson),
    # url(r'^establecimiento/editarEstablecimiento/(?P<id>[0-9]+)/$', views.formularioEditarEstablecimiento),
    url(r'^establecimiento/registrarEstablecimientos/$', viewEst.formularioRegistrarEstablecimiento),

    # ---------
    # Administracion de Municipios
    url(r'^configuracion/Municipios/$', views.indexMunicipios),
    url(r'^configuracion/MunicipioJson/$', views.MunicipiosJson),
    url(r'^configuracion/editarMunicipio/(?P<id>[0-9]+)/$', views.formularioEditarMunicipio),
    url(r'^configuracion/registrarMunicipio/$', views.formularioRegistrarMunicipio),
    # ---------
    # Administracion de tipos relaciones familiares
    url(r'^configuracion/Personas/$', views.Personas),
    url(r'^configuracion/PersonasJson/$', views.PersonasJson),
    url(r'^configuracion/editarPersonas/(?P<id>[0-9]+)/$', views.formularioEditarPersonas),
    url(r'^configuracion/registrarPersonas/$', views.formularioRegistrarPersonas),
    # ---------
    # Administracion de tipos relaciones familiares
    url(r'^configuracion/departamentos/$', views.departamentos),
    url(r'^configuracion/departamentosJson/$', views.departamentosJson),
    url(r'^configuracion/editardepartamentos/(?P<id>[0-9]+)/$', views.editardepartamentos),
    url(r'^configuracion/editardepartamentosPost/$', views.editardepartamentosPost),
    url(r'^configuracion/nuevodepartamentos/$', views.formNuevodepartamentos),
    url(r'^configuracion/nuevodepartamentosPost/$', views.nuevodepartamentosPost),    
    # ---------
    # Administracion de tipos relaciones familiares
    url(r'^configuracion/relacionesFamiliares/$', views.relacionesFamiliares),
    url(r'^configuracion/relacionesFamiliaresJson/$', views.relacionesFamiliaresJson),
    url(r'^configuracion/editarrelacionesFamiliares/(?P<id>[0-9]+)/$', views.editarrelacionesFamiliares),
    url(r'^configuracion/editarrelacionesFamiliaresPost/$', views.editarrelacionesFamiliaresPost),
    url(r'^configuracion/nuevorelacionesFamiliares/$', views.formNuevorelacionesFamiliares),
    url(r'^configuracion/nuevorelacionesFamiliaresPost/$', views.nuevorelacionesFamiliaresPost),
    # ---------
    # Administracion de tipos de documentos
    url(r'^configuracion/tiposDocumentos/$', views.tiposDocumentos),
    url(r'^configuracion/tiposDocumentosJson/$', views.tiposDocumentosJson),
    url(r'^configuracion/editartiposDocumentos/(?P<id>[0-9]+)/$', views.editartiposDocumentos),
    url(r'^configuracion/editartiposDocumentosPost/$', views.editartiposDocumentosPost),
    url(r'^configuracion/nuevotiposDocumentos/$', views.formNuevoTipoDocumento),
    url(r'^configuracion/nuevotiposDocumentosPost/$', views.nuevotiposDocumentosPost),
    # --------
    # Consultas comunes
    url(r'^configuracion/consulta/$', views.consulta_configuracion)
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)