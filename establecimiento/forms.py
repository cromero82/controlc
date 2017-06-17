from django import forms
from models import Establecimientos, Sedes, Jornadas, Nivelesaprobados
from django.utils.translation import gettext_lazy as _
from django.forms import Field
from django.utils.translation import ugettext

ESTREGISTRO_TYPES = (
    (1, 'Activo'),
    (2, 'Inactivo'),)


class EstablecimientoForm(forms.ModelForm):
    class Meta:
        model = Establecimientos
        fields = ['id', 'nombre', 'codigo', 'nombreRector',
                  'municipio', 'fechafundacion', 'escudo']
        labels = {'nombre': _('Nombre establecimiento educativo'),
                  'codigo': _('Codigo DANE'),
                  'nombreRector': _('Nombre del rector'), 'municipio': _('Municipio / Ciudad'),
                  'numsedes': _('Numero de sedes'), 'fechafundacion': _('Fecha de fundacion'),
                  'escudo': _('Escudo')
                  }


class SedesForm(forms.ModelForm):
    class Meta:
        model = Sedes
        fields = ['establecimiento', 'nombre', 'codigo', 'direccion',
                  'telefono', 'correoelectronico', 'responsable']
        labels = {'establecimiento': _('Establecimiento'), 'nombre': _('Nombre de la sede'),
                  'codigo': _('Consecutivo DANE sede'), 'direccion': _('Direccion'),
                  'telefono': _('Telefono'), 'correoelectronico': _('Correo electronico'),
                  'responsable': _('Nombre de persona a cargo'), 'municipio': _('Municipio / Ciudad')
                  }


class JornadasForm(forms.ModelForm):
    estregistro = forms.ChoiceField(
        required=True, label='Estado del registro', choices=ESTREGISTRO_TYPES)

    class Meta:
        model = Jornadas
        fields = ['sede', 'jornada', 'estregistro']
        labels = {'sede': _('Sede'), 'jornada': _('Jornada'),
                  'estregistro': _('Estado')
                  }

class NivelesaprobadosForm(forms.ModelForm):
    estregistro = forms.ChoiceField(
        required=True, label='Estado del registro', choices=ESTREGISTRO_TYPES)
    class Meta:
        model = Nivelesaprobados
        fields = ['id', 'establecimiento', 'nivel', 'tipoaprobacion', 'numeroActo', 'fecha','anexo']
        labels = {
            'establecimiento': _('Establecimiento educativo'), 
            'nivel': _('Nivel academico'), 'tipoaprobacion': _('Tipo de acto administrativo'),
            'numeroActo': _('Numero acto administrativo'),
            'fecha': _('Fecha acto administrativo'), 'anexo': _('Anexo digitalizado')
        }
        widgets = {
            'numeroActo': forms.TextInput({'placeholder': 'Ingrese numero de acto administrativo'})
        }