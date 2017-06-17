from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.template.loader import render_to_string
import unicodedata
from django.db import IntegrityError

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

def ejecucionAdminDataBase(form, request, accion, datoReferencia):
    data = dict()
    data['transaccion'] = True
    if (form.is_valid()):
        try:
            modelData = form.save()
            # form.save()
            data['dato'] = modelData.id
            data['mensaje'] = "La operacion " + accion + \
                " " + datoReferencia + " se ha ejecutado correctamente."
        except IntegrityError, err:
            data['transaccion'] = False
            data['mensaje'] = "ya existe"
        except Exception,  err:
            data['transaccion'] = False
            data['mensaje'] = err.message
    else:
        data['transaccion'] = False
        messages.error(request, "Error")
    return data

def ejecucionAdminDataBaseVal(form, request, accion, datoReferencia, nombreFormulario):
    data = dict()
    data['transaccion'] = True
    if (form.is_valid()):
        try:
            form.save()
            data['mensaje'] = "La operacion " + accion + \
                " " + datoReferencia + " se ha ejecutado correctamente."
        except IntegrityError, err:
            data['transaccion'] = False
            data['mensaje'] = "ya existe"
            context = {'form': form}
            data['html_form'] = render_to_string(
            nombreFormulario, context, request=request)
        except Exception,  err:
            data['transaccion'] = False
            data['mensaje'] = err.message
            context = {'form': form}
            data['html_form'] = render_to_string(
            nombreFormulario, context, request=request)
    else:
        data['transaccion'] = False
        messages.error(request, "Error")
        context = {'form': form}
        data['html_form'] = render_to_string(
        nombreFormulario, context, request=request)
    return data

def mensajeSalida(datos):
    data = dict()
    data['transaccion'] = True
    data['datos'] = datos
    return data

def formularioAdmin(form, nombreFormulario, tituloFormulario, request):
    data = dict()
    data['transaccion'] = True
    data['titulo'] = tituloFormulario    
    context = {'form': form}
    data['html_form'] = render_to_string(
        nombreFormulario, context, request=request)
    return data