from django import forms
from models import Establecimientos, Sedes
from django.utils.translation import gettext_lazy as _
from django.forms import Field
from django.utils.translation import ugettext


class EstablecimientoForm(forms.ModelForm):
    class Meta:
        model = Establecimientos
        fields = ['id', 'nombre', 'codigo','nombreRector','municipio'
        ,'fechafundacion', 'escudo']
        labels = {'nombre': _('Nombre establecimiento educativo'), 
        'codigo': _('Codigo DANE'),         
        'nombreRector': _('Nombre del rector'), 'municipio': _('Municipio / Ciudad'),
        'numsedes': _('Numero de sedes'), 'fechafundacion': _('Fecha de fundacion'),
        'escudo': _('Escudo')
        }

class SedesForm(forms.ModelForm):
    class Meta:
        model = Sedes
        fields = ['establecimiento', 'nombre', 'codigo', 'direccion','telefono','correoelectronico','responsable']
        labels = {'establecimiento': _('Establecimiento'), 'nombre': _('Nombre de la sede'), 
        'codigo': _('Consecutivo DANE sede'), 'direccion': _('Direccion'), 
        'telefono': _('Telefono'), 'correoelectronico': _('Correo electronico'),
        'responsable': _('Nombre de persona a cargo'), 'municipio': _('Municipio / Ciudad')
        }