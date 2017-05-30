from django import forms
from models import Establecimientos
from django.utils.translation import gettext_lazy as _
from django.forms import Field
from django.utils.translation import ugettext

class EstablecimientoForm(forms.ModelForm):
    class Meta:
        model = Establecimientos
        fields = ['id', 'nombre', 'codigo', 'direccion','telefono','correoelectronico','nombreRector','municipio']
        labels = {'nombre': _('Nombre establecimiento educativo'), 
        'codigo': _('Codigo DANE'), 'direccion': _('Direccion'),
        'telefono': _('Telefono'), 'correoelectronico': _('Correo electronico'),
        'nombreRector': _('Nombre del rector'), 'municipio': _('Municipio / Ciudad'),
        'numsedes': _('Numero de sedes')
        }
