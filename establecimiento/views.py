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
from establecimiento.models import Establecimientos, Sedes

# Importando Forms
from forms import EstablecimientoForm, SedesForm
import sys
from configuracion.miUtils import ejecucionAdminDataBase, formularioAdmin, remove_accents
from configuracion.miUtils import ejecucionAdminDataBaseVal
from django.contrib import messages
from django.http import JsonResponse
from django.template.context_processors import csrf


# ----------------------------------------------
#  Sedes
@login_required(login_url='/accounts/login/')
def formularioEditarSedes(request, id):
    if request.method == 'POST':
        datos = get_object_or_404(Sedes, pk=id)
        form = SedesForm(request.POST,  request.FILES or None, instance=datos)
        data = ejecucionAdminDataBaseVal(
            form, request, "Edicion grado", request.POST['nombre'], "formSedes.html")
        return JsonResponse(data)
    else:
        datos = get_object_or_404(Sedes, pk=id)
        form = SedesForm(instance=datos)
        return JsonResponse(formularioAdmin(form, "formSedes.html", "Edicion de sede", request))


@login_required(login_url='/accounts/login/')
def formularioRegistrarSedes(request):
    if request.method == 'POST':
        form = SedesForm(request.POST, request.FILES or None)
        data = ejecucionAdminDataBaseVal(
            form, request, "Registrar sede", request.POST['nombre'], "formSedes.html")
        return JsonResponse(data)
    else:
        form = SedesForm()
        return JsonResponse(formularioAdmin(form, "formSedes.html", "Registre datos de la sede", request))


@login_required(login_url='/accounts/login/')
def SedesJson(request):
    lista_datos = Sedes.objects.filter(
        establecimiento=request.GET['establecimiento']
    ).order_by('codigo')
    json = serializers.serialize(
        'json', lista_datos, use_natural_foreign_keys=True)
    return HttpResponse(json, content_type='application/json')

# --- No aplica, sin index por ahora.
# @login_required(login_url='/accounts/login/')
# def indexSedes(request):
#     return render(request, 'Sedes.html', context={'datos': ''})


# ---------
# Administracion de Establecimiento

@login_required(login_url='/accounts/login/')
def perfilEstablecimiento(request, id):
    establecimiento = get_object_or_404(Establecimientos, pk=id)
    form = EstablecimientoForm(request.POST,  request.FILES or None, instance=establecimiento)
    return render(request, 'perfilEstablecimiento.html', context={'form': form})
# --------------------
def formularioRapidoEstablecimiento(request):
    form = EstablecimientoForm()
    return render(request, 'formRapidoEstablecimiento.html', context={'form': form})


def formularioNuevoEstablecimientos(request):
    form = EstablecimientoForm()
    return render(request, 'formModoRegistroEstablecimiento.html', context={'form': form})


@login_required(login_url='/accounts/login/')
def formularioEditarEstablecimiento(request, id):
    if request.method == 'POST':
        establecimiento = get_object_or_404(Establecimientos, pk=id)
        form = EstablecimientoForm(
            request.POST,  request.FILES or None, instance=establecimiento)
        data = ejecucionAdminDataBase(
            form, request, "Edicion establecimiento", request.POST['nombre'])
        return JsonResponse(data)
    else:
        establecimiento = get_object_or_404(Establecimientos, pk=id)
        form = EstablecimientoForm(instance=establecimiento)
        return JsonResponse(formularioAdmin(form, "formEstablecimiento.html", "Edicion de establecimiento", request))


def formularioRegistrarEstablecimiento(request):
    if request.method == 'POST':
        form = EstablecimientoForm(request.POST, request.FILES or None)
        data = ejecucionAdminDataBase(
            form, request, "Registrar establecimiento", request.POST['nombre'])
        return JsonResponse(data)
    else:
        form = EstablecimientoForm()
        return JsonResponse(formularioAdmin(form, "formEstablecimiento.html", "Registre datos generales", request))


def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]


def EstablecimientosJson(request):
    if request.GET['nombre'] != '':
        lista_datos = Establecimientos.objects.filter(
            estregistro=request.GET['estregistro'],
            nombre__contains=remove_accents(request.GET['nombre'].upper())
        )
    else:
        lista_datos = Establecimientos.objects.filter(
            estregistro=request.GET['estregistro']
        )
    json = serializers.serialize(
        'json', lista_datos,  use_natural_foreign_keys=True)
    return HttpResponse(json, content_type='application/json')


@login_required(login_url='/accounts/login/')
def indexEstablecimientos(request):
    return render(request, 'Establecimientos.html', context={'datos': ''})
