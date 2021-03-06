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
from configuracion import views as viewConf
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

    # ---------
    # NivelesAprobados    
    url(r'^establecimiento/consultarFile/$', viewEst.consultaArchivos),
    url(r'^establecimiento/NivelesAprobadosJson/$', viewEst.NivelesAprobadosJson),
    url(r'^establecimiento/editarNivelesAprobados/(?P<id>[0-9]+)/$', viewEst.formularioEditarNivelesAprobados),
    url(r'^establecimiento/registrarNivelesAprobados/$', viewEst.formularioRegistrarNivelesAprobados),

    # ---------
    # Jornadas    
    url(r'^establecimiento/JornadasJson/$', viewEst.JornadasJson),
    url(r'^establecimiento/editarJornadas/(?P<id>[0-9]+)/$', viewEst.formularioEditarJornadas),
    url(r'^establecimiento/registrarJornadas/$', viewEst.formularioRegistrarJornadas),

    # ---------
    # Sedes
    # url(r'^establecimiento/Sedes/$', viewConf.indexSedes),
    url(r'^establecimiento/SedesJson/$', viewEst.SedesJson),
    url(r'^establecimiento/editarSedes/(?P<id>[0-9]+)/$', viewEst.formularioEditarSedes),
    url(r'^establecimiento/registrarSedes/$', viewEst.formularioRegistrarSedes),

    # ---------
    # Administracion de Establecimientos    
    url(r'^establecimiento/perfilEstablecimiento/(?P<id>[0-9]+)/$', viewEst.perfilEstablecimiento),
    # -----
    url(r'^establecimiento/RegistroRapido/$', viewEst.formularioRapidoEstablecimiento),
    url(r'^establecimiento/editarRapidoEstablecimiento/(?P<id>[0-9]+)/$', viewEst.formularioEditarEstablecimiento),
    url(r'^establecimiento/RegistrarRapidoEstablecimiento/$', viewEst.formularioRegistrarEstablecimiento),
    url(r'^establecimiento/nuevoEstablecimiento/$', viewEst.formularioNuevoEstablecimientos),
    url(r'^establecimiento/Establecimientos/$', viewEst.indexEstablecimientos),
    url(r'^establecimiento/EstablecimientosJson/$', viewEst.EstablecimientosJson),    
    url(r'^establecimiento/registrarEstablecimientos/$', viewEst.formularioNuevoEstablecimientos),

    #----------
    # Inicio de sesion
    url(r'^login/$', viewConf.ingresar, name='login'),
    url(r'^auth/$', viewConf.ingresar, name='ingresar'),
    url(r'^accounts/login/$', viewConf.ingresar, name='ingresar'),
    url(r'^cerrar/$', viewConf.cerrar, name='cerrar'),
    url(r'^ingresar/$', viewConf.ingresar, name='ingresar'),

    # ---------
    # Parametricas Tipo de jornadas impartidas
    url(r'^configuracion/TfuenteRecursos/$', viewConf.indexTfuenteRecursos),
    url(r'^configuracion/TfuenteRecursosJson/$', viewConf.TfuenteRecursosJson),
    url(r'^configuracion/editarTfuenteRecursos/(?P<id>[0-9]+)/$', viewConf.formularioEditarTfuenteRecursos),
    url(r'^configuracion/registrarTfuenteRecursos/$', viewConf.formularioRegistrarTfuenteRecursos),

    # ---------
    # Parametricas Tipo Acto administrativo
    url(r'^configuracion/Tactoadmins/$', viewConf.indexTactoadmins),
    url(r'^configuracion/TactoadminsJson/$', viewConf.TactoadminsJson),
    url(r'^configuracion/editarTactoadmin/(?P<id>[0-9]+)/$', viewConf.formularioEditarTactoadmins),
    url(r'^configuracion/registrarTactoadmin/$', viewConf.formularioRegistrarTactoadmins),

    # ---------
    # Parametricas Niveles educativos
    url(r'^configuracion/Niveles/$', viewConf.indexNiveles),
    url(r'^configuracion/NivelesJson/$', viewConf.NivelesJson),
    url(r'^configuracion/editarNiveles/(?P<id>[0-9]+)/$', viewConf.formularioEditarNiveles),
    url(r'^configuracion/registrarNiveles/$', viewConf.formularioRegistrarNiveles),

    # ---------
    # Parametricas Grados
    url(r'^configuracion/Grados/$', viewConf.indexGrados),
    url(r'^configuracion/GradosJson/$', viewConf.GradosJson),
    url(r'^configuracion/editarGrados/(?P<id>[0-9]+)/$', viewConf.formularioEditarGrados),
    url(r'^configuracion/registrarGrados/$', viewConf.formularioRegistrarGrados),

    # ---------
    # Parametricas Tipo de jornadas impartidas
    url(r'^configuracion/Tcaracteres/$', viewConf.indexTcaracteres),
    url(r'^configuracion/TcaracteresJson/$', viewConf.TcaracteresJson),
    url(r'^configuracion/editarTcaracter/(?P<id>[0-9]+)/$', viewConf.formularioEditarTcaracter),
    url(r'^configuracion/registrarTcaracter/$', viewConf.formularioRegistrarTcaracter),

    # ---------
    # Parametricas Tipo de jornadas impartidas
    url(r'^configuracion/Tjornadas/$', viewConf.indexTjornadas),
    url(r'^configuracion/TjornadasJson/$', viewConf.TjornadasJson),
    url(r'^configuracion/editarTjornada/(?P<id>[0-9]+)/$', viewConf.formularioEditarTjornada),
    url(r'^configuracion/registrarTjornada/$', viewConf.formularioRegistrarTjornada),

    # ---------
    # Parametricas Especialidad de la media
    url(r'^configuracion/Especialidades/$', viewConf.indexEspecialidades),
    url(r'^configuracion/EspecialidadesJson/$', viewConf.EspecialidadsJson),
    url(r'^configuracion/editarEspecialidad/(?P<id>[0-9]+)/$', viewConf.formularioEditarEspecialidad),
    url(r'^configuracion/registrarEspecialidad/$', viewConf.formularioRegistrarEspecialidad),

    # ---------
    # Parametricas Metodologias
    url(r'^configuracion/Metodologias/$', viewConf.indexMetodologias),
    url(r'^configuracion/MetodologiasJson/$', viewConf.MetodologiasJson),
    url(r'^configuracion/editarMetodologia/(?P<id>[0-9]+)/$', viewConf.formularioEditarMetodologia),
    url(r'^configuracion/registrarMetodologia/$', viewConf.formularioRegistrarMetodologia),

    # ---------
    # Administracion de Municipios
    url(r'^configuracion/Municipios/$', viewConf.indexMunicipios),
    url(r'^configuracion/MunicipioJson/$', viewConf.MunicipiosJson),
    url(r'^configuracion/editarMunicipio/(?P<id>[0-9]+)/$', viewConf.formularioEditarMunicipio),
    url(r'^configuracion/registrarMunicipio/$', viewConf.formularioRegistrarMunicipio),
    url(r'^configuracion/getCodigoMunicipio/(?P<nombreMunicipio>[0-9]+)/$', viewConf.getMunicipio),
    # ---------
    # Administracion de tipos relaciones familiares
    url(r'^configuracion/Personas/$', viewConf.Personas),
    url(r'^configuracion/PersonasJson/$', viewConf.PersonasJson),
    url(r'^configuracion/editarPersonas/(?P<id>[0-9]+)/$', viewConf.formularioEditarPersonas),
    url(r'^configuracion/registrarPersonas/$', viewConf.formularioRegistrarPersonas),
    # ---------
    # Administracion de tipos relaciones familiares
    url(r'^configuracion/departamentos/$', viewConf.departamentos),
    url(r'^configuracion/departamentosJson/$', viewConf.departamentosJson),
    url(r'^configuracion/editardepartamentos/(?P<id>[0-9]+)/$', viewConf.editardepartamentos),
    url(r'^configuracion/editardepartamentosPost/$', viewConf.editardepartamentosPost),
    url(r'^configuracion/nuevodepartamentos/$', viewConf.formNuevodepartamentos),
    url(r'^configuracion/nuevodepartamentosPost/$', viewConf.nuevodepartamentosPost),    
    # ---------
    # Administracion de tipos relaciones familiares
    url(r'^configuracion/relacionesFamiliares/$', viewConf.relacionesFamiliares),
    url(r'^configuracion/relacionesFamiliaresJson/$', viewConf.relacionesFamiliaresJson),
    url(r'^configuracion/editarrelacionesFamiliares/(?P<id>[0-9]+)/$', viewConf.editarrelacionesFamiliares),
    url(r'^configuracion/editarrelacionesFamiliaresPost/$', viewConf.editarrelacionesFamiliaresPost),
    url(r'^configuracion/nuevorelacionesFamiliares/$', viewConf.formNuevorelacionesFamiliares),
    url(r'^configuracion/nuevorelacionesFamiliaresPost/$', viewConf.nuevorelacionesFamiliaresPost),
    # ---------
    # Administracion de tipos de documentos
    url(r'^configuracion/tiposDocumentos/$', viewConf.tiposDocumentos),
    url(r'^configuracion/tiposDocumentosJson/$', viewConf.tiposDocumentosJson),
    url(r'^configuracion/editartiposDocumentos/(?P<id>[0-9]+)/$', viewConf.editartiposDocumentos),
    url(r'^configuracion/editartiposDocumentosPost/$', viewConf.editartiposDocumentosPost),
    url(r'^configuracion/nuevotiposDocumentos/$', viewConf.formNuevoTipoDocumento),
    url(r'^configuracion/nuevotiposDocumentosPost/$', viewConf.nuevotiposDocumentosPost),
    # --------
    # Consultas comunes
    url(r'^configuracion/consulta/$', viewConf.consulta_configuracion)
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)