from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.template.loader import render_to_string
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

def ejecucionAdminDataBase(form, request, accion, datoReferencia):
    data = dict()
    data['transaccion'] = True
    if form.is_valid:
        try:
            form.save()
            data['mensaje'] = "La operacion " + accion + \
                " " + datoReferencia + " se ha ejecutado correctamente."
        except Exception, err:
            data['transaccion'] = False
            data['mensaje'] = err.message
    else:
        data['transaccion'] = False
        messages.error(request, "Error")
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