from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
# Autenticacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
# Models
from datetime import datetime
# from models import Persona
from models import Tdocumento
from models import TRelacionFamiliar
from models import Departamento, Persona, Municipios, Metodologia
# Importando Forms
from forms import DepartamentoForm, PersonaForm, MunicipioForm, MetodologiaForm
import sys
import miUtils
from miUtils import ejecucionAdminDataBaseVal
from miUtils import ejecucionAdminDataBase, formularioAdmin, remove_accents
from django.contrib import messages
from django.http import JsonResponse
from django.template.context_processors import csrf

# ---------
# Administracion de parametricas EE
@login_required(login_url='/accounts/login/')
def formularioEditarMetodologia(request, id):   
    if request.method == 'POST': 
        metodologia = get_object_or_404(Metodologia, pk=id)
        form = MetodologiaForm(request.POST,  request.FILES or None,instance=metodologia)
        data = ejecucionAdminDataBase(form, request, "Edicion metodologia", request.POST['nombre'])
        return JsonResponse(data)
    else:  
        metodologia = get_object_or_404(Metodologia, pk=id)
        form = MetodologiaForm(instance=metodologia)      
        return JsonResponse(formularioAdmin(form, "formMetodologia.html", "Edicion de metodologia", request))

def formularioRegistrarMetodologia(request):
    if request.method == 'POST':
        form = MetodologiaForm(request.POST, request.FILES or None)
        data = ejecucionAdminDataBaseVal(form, request, "Registrar metodologia", request.POST['nombre'],"formMetodologia.html")
        return JsonResponse(data)
    else:
        form = MetodologiaForm()
        return JsonResponse(formularioAdmin(form, "formMetodologia.html", "Registre datos metodologia", request))

def MetodologiasJson(request):
    if request.GET['nombre'] != '':
        lista_datos = Metodologia.objects.filter(
            estregistro=request.GET['estregistro'],
            nombre__contains=remove_accents(request.GET['nombre'].upper())
        )
    else:
        lista_datos = Metodologia.objects.filter(
            estregistro=request.GET['estregistro']
        )        
    json = serializers.serialize('json', lista_datos,  use_natural_foreign_keys=True)
    return HttpResponse(json, content_type='application/json')

@login_required(login_url='/accounts/login/')
def indexMetodologias(request):    
    return render(request, 'Metodologias.html', context = { 'datos': '' })

# ---------
# Control de inicio de sesion
def cerrar(request):
    logout(request)
    #render(request, 'afiliados/salida.html')
    return HttpResponseRedirect('/ingresar')
    
def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/configuracion/Personas')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/configuracion/Personas')
                else:
                    return render(request, 'afiliados/noactivo.html')
            else:
                return render(request, 'afiliados/nousuario.html')
    else:
        formulario = AuthenticationForm()
    context = {'formulario': formulario}
    return render(request, 'cuentasUsuario/pages_login.html', context)

# Formulario de login
def milogin(request):
    formulario = AuthenticationForm()
    context = {'formulario': formulario}
    return render(request, 'cuentasUsuario/pages_login.html', context)
    
def index(request):    
    return render(request, 'Municipios.html', context = { 'datos': '' })


# ---------
# Consultas personalizadas
def consulta_configuracion(request):   
    data = dict()
    data['transaccion'] = True    
    try:
        if request.POST["tipoConsulta"] == 'codigoDepartamento':
            datos = get_object_or_404(Departamento, pk=request.POST["dato"])
            data['datos'] =  {'misDatos': datos.codigo}
        elif request.POST["tipoConsulta"] == 'otra cosa':
            datos = get_object_or_404(Departamento, pk=request.POST["dato"])       
    except Exception, err:
        data['transaccion'] = False
        data['mensaje'] = err.message
    return  JsonResponse(data)
    
# ---------
# Administracion de Municipio
@login_required(login_url='/accounts/login/')
def formularioEditarMunicipio(request, id):   
    if request.method == 'POST': 
        municipio = get_object_or_404(Municipios, pk=id)
        form = MunicipioForm(request.POST,  request.FILES or None,instance=municipio)
        data = ejecucionAdminDataBase(form, request, "Edicion municipio", request.POST['nombre'])
        return JsonResponse(data)
    else:  
        municipio = get_object_or_404(Municipios, pk=id)
        form = MunicipioForm(instance=municipio)      
        return JsonResponse(formularioAdmin(form, "formMunicipio.html", "Edicion de municipio", request))

def formularioRegistrarMunicipio(request):
    if request.method == 'POST':
        form = MunicipioForm(request.POST, request.FILES or None)
        data = ejecucionAdminDataBase(form, request, "Registrar municipio", request.POST['nombre'])
        return JsonResponse(data)
    else:
        form = MunicipioForm()
        return JsonResponse(formularioAdmin(form, "formMunicipio.html", "Registre datos generales", request))
def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

def MunicipiosJson(request):
    if request.GET['nombre'] != '':
        lista_datos = Municipios.objects.filter(
            estregistro=request.GET['estregistro'],
            nombre__contains=remove_accents(request.GET['nombre'].upper())
        )
    else:
        lista_datos = Municipios.objects.filter(
            estregistro=request.GET['estregistro']
        )        
    json = serializers.serialize('json', lista_datos,  use_natural_foreign_keys=True)
    return HttpResponse(json, content_type='application/json')

@login_required(login_url='/accounts/login/')
def indexMunicipios(request):    
    return render(request, 'Municipios.html', context = { 'datos': '' })

# ---------
# Administracion de Personas
def formularioEditarPersonas(request, id):   
    if request.method == 'POST': 
        persona = get_object_or_404(Persona, pk=id)
        form = PersonaForm(request.POST,  request.FILES or None,instance=persona)
        data = ejecucionAdminDataBase(form, request, "Edicion datos personales", request.POST['nombres'])
        return JsonResponse(data)
    else:  
        persona = get_object_or_404(Persona, pk=id)
        form = PersonaForm(instance=persona)      
        return JsonResponse(formularioAdmin(form, "registrarPersona.html", "Edicion de datos personales", request))

def formularioRegistrarPersonas(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST, request.FILES or None)
        data = ejecucionAdminDataBase(form, request, "Registrar persona", request.POST['nombres'])
        return JsonResponse(data)
    else:
        form = PersonaForm()
        return JsonResponse(formularioAdmin(form, "registrarPersona.html", "Registre datos generales", request))

def PersonasJson(request):
    if request.GET['nombre'] != '':
        lista_datos = Persona.objects.filter(
            estregistro=request.GET['estregistro'],
            nombres__contains=remove_accents(request.GET['nombre'].upper())
        )
    else:
        lista_datos = Persona.objects.filter(
            estregistro=request.GET['estregistro']
        )
    json = serializers.serialize('json', lista_datos)
    return HttpResponse(json, content_type='application/json')

@login_required(login_url='/accounts/login/')
def Personas(request):
    context = {
        'datos': ''
    }
    return render(request, 'Personas.html', context)


# ---------
# Administracion de departamentos
def nuevodepartamentosPost(request):
    data = dict()
    data['transaccion'] = True
    form = DepartamentoForm(request.POST)
    if form.is_valid:
        form.save()
        data['mensaje'] = "creacion de departamento: " + \
            request.POST['nombre'] + " ejecutada satisfactoriamente."
    else:
        data['transaccion'] = False
        messages.error(request, "Error")
        #data['mensaje']= err.message
    return JsonResponse(data)


def formNuevodepartamentos(request):
    data = dict()
    data['transaccion'] = True
    form = DepartamentoForm()
    context = {'form': form}
    data['html_form'] = render_to_string(
        'nuevodepartamentos.html', context, request=request)
    return JsonResponse(data)


def editardepartamentosPost(request):
    data = dict()
    data['transaccion'] = True
    departamento = get_object_or_404(Departamento, pk=request.POST['id'])
    form = DepartamentoForm(request.POST, instance=departamento)
    if form.is_valid:
        form.save()
        data['mensaje'] = "actualizacion de departamento: " + \
            request.POST['nombre'] + " ejecutada satisfactoriamente."
    else:
        data['transaccion'] = False
        messages.error(request, "Error")
    return JsonResponse(data)


def editardepartamentos(request, id):
    data = dict()
    data['transaccion'] = True
    try:
        departamento = get_object_or_404(Departamento, pk=id)
        form = DepartamentoForm(instance=departamento)
        context = {'form': form}
        data['html_form'] = render_to_string(
            'editardepartamentos.html', context, request=request)
        context = {'form': form}
    except ObjectDoesNotExist:
        # except  #Persona.DoesNotExist:
        data['transaccion'] = False
        data['mensaje'] = "No fue tipo de relacion familiar"
    return JsonResponse(data)


def departamentosJson(request):
    if request.GET['nombre'] != '':
        lista_datos = Departamento.objects.filter(
            estregistro=request.GET['estregistro'],
            nombre__contains=remove_accents(request.GET['nombre'].upper())
        )
    else:
        lista_datos = Departamento.objects.filter(
            estregistro=request.GET['estregistro']
        )
    json = serializers.serialize('json', lista_datos)
    return HttpResponse(json, content_type='application/json')


def departamentos(request):
    context = {
        'datos': ''
    }
    return render(request, 'departamentos.html', context)

# ---------
# Administracion de tipos relaciones familiares


def nuevorelacionesFamiliaresPost(request):
    data = dict()
    data['transaccion'] = True
    try:
        datos = TRelacionFamiliar(
            nombre=request.POST['nombre'],
            estregistro=request.POST['estregistro'])
        datos.save()
        data['mensaje'] = "creacion relacion Familiar: " + \
            request.POST['nombre'] + " ejecutada satisfactoriamente."
    except Exception, err:
        data['transaccion'] = False
        data['mensaje'] = err.message
    return JsonResponse(data)


def formNuevorelacionesFamiliares(request):
    data = dict()
    data['transaccion'] = True
    # context = {'datos': ''}
    data['html_form'] = render_to_string(
        'nuevorelacionesFamiliares.html', request=request)
    return JsonResponse(data)


def editarrelacionesFamiliaresPost(request):
    data = dict()
    data['transaccion'] = True
    try:
        datos = TRelacionFamiliar.objects.get(pk=request.POST['id'])
        datos.nombre = request.POST['nombre']
        datos.estregistro = request.POST['estregistro']
        datos.save()
        data['mensaje'] = "edicion de relacion Familiar: " + \
            datos.nombre + " ejecutada satisfactoriamente."
    except Exception, err:
        data['transaccion'] = False
        data['mensaje'] = err.message
    return JsonResponse(data)


def editarrelacionesFamiliares(request, id):
    data = dict()
    data['transaccion'] = True
    try:
        datos = TRelacionFamiliar.objects.get(pk=id)
        context = {'datos': datos}
        data['html_form'] = render_to_string(
            'editarrelacionesFamiliares.html', context, request=request)
    except Exception, err:
        data['transaccion'] = False
        data['mensaje'] = err.message
    return JsonResponse(data)


def relacionesFamiliaresJson(request):
    if request.GET['nombre'] != '':
        lista_datos = TRelacionFamiliar.objects.filter(
            estregistro=request.GET['estregistro'],
            nombre__contains=remove_accents(request.GET['nombre'].upper())
        )
    else:
        lista_datos = TRelacionFamiliar.objects.filter(
            estregistro=request.GET['estregistro']
        )
    json = serializers.serialize('json', lista_datos)
    return HttpResponse(json, content_type='application/json')


def relacionesFamiliares(request):
    context = {
        'datos': ''
    }
    return render(request, 'relacionesFamiliares.html', context)


# ---------
# Administracion de tipos de documentos
def nuevotiposDocumentosPost(request):
    data = dict()
    data['transaccion'] = True
    try:
        datos = Tdocumento(
            nombre=request.POST['nombre'],
            sigla=request.POST['sigla'],
            estregistro=request.POST['estregistro'])
        datos.save()
        data['mensaje'] = "creacion tipo de documento: " + \
            request.POST['nombre'] + " ejecutada satisfactoriamente."
    except Exception, err:
        data['transaccion'] = False
        data['mensaje'] = err.message
    return JsonResponse(data)


def formNuevoTipoDocumento(request):
    data = dict()
    data['transaccion'] = True
    # context = {'datos': ''}
    data['html_form'] = render_to_string(
        'nuevotiposDocumentos.html', request=request)
    return JsonResponse(data)


def editartiposDocumentosPost(request):
    data = dict()
    data['transaccion'] = True
    try:
        datos = Tdocumento.objects.get(pk=request.POST['id'])
        datos.nombre = request.POST['nombre']
        datos.sigla = request.POST['sigla']
        datos.estregistro = request.POST['estregistro']
        datos.save()
        data['mensaje'] = "edicion de tipo de documento: " + \
            datos.nombre + " ejecutada satisfactoriamente."
    except Exception, err:
        data['transaccion'] = False
        data['mensaje'] = err.message
    return JsonResponse(data)


def editartiposDocumentos(request, id):
    data = dict()
    data['transaccion'] = True
    try:
        datos = Tdocumento.objects.get(pk=id)
        context = {'datos': datos}
        data['html_form'] = render_to_string(
            'editartiposDocumentos.html', context, request=request)
    except ObjectDoesNotExist:
        # except  #Persona.DoesNotExist:
        data['transaccion'] = False
        data['mensaje'] = "No fue tipo de relacion familiar"
    return JsonResponse(data)


def tiposDocumentosJson(request):
    if request.GET['nombre'] != '':
        lista_datos = Tdocumento.objects.filter(
            estregistro=request.GET['estregistro'],
            nombre__contains=remove_accents(request.GET['nombre'].upper())
        )
    else:
        lista_datos = Tdocumento.objects.filter(
            estregistro=request.GET['estregistro']
        )
    json = serializers.serialize('json', lista_datos)
    return HttpResponse(json, content_type='application/json')


def tiposDocumentos(request):
    context = {
        'datos': ''
    }
    return render(request, 'tiposDocumentos.html', context)
