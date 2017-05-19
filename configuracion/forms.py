from django import forms
from models import Persona, Municipios, Metodologia, Especialidad
from models import Departamento
from django.utils.translation import gettext_lazy as _
from django.forms import Field
from django.utils.translation import ugettext
# Field.default_error_messages = {
#     'required': ugettext("This field is mandatory.xxx"),
# }
ESTREGISTRO_TYPES = (
    (1, 'Activo'),
    (2, 'Inactivo'),
)

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['id', 'foto', 'nombres', 'apellidos', 'numerodocumento', 'numerodocumento',
                  'tdocumento', 'direccion', 'telefono', 'fechanacimiento', 'correoelectronico']
        labels = {
            'nombres': _('Nombres'), 'apellidos': _('Apellidos'),
            'numerodocumento': _('Numero documento'), 'tdocumento': _('Tipo documento'),
            'direccion': _('Direccion'), 'telefono': _('Telefono'),
            'fechanacimiento': _('Fecha nacimiento'), 'correoelectronico': _('Email')
        }


class MunicipioForm(forms.ModelForm):
    estregistro = forms.ChoiceField(
        required=True, label='Estado del registro', choices=ESTREGISTRO_TYPES)

    class Meta:
        model = Municipios
        fields = ['codigo','nombre',  'departamento', 'estregistro']
        labels = {
            'codigo': _('Codigo DANE'),
            'nombre': _('Nombres'), 'departamento': _('Departamento'), 'estregistro': _('Estado registro'),
        }
        error_messages = {
            'codigo': {
                'required': _("Please enter your mobile numberrrrrrrrrrrrrrr."),
            },
            'nombre': {
                'required': _("Please enter your bio."),
            }
        }

class DepartamentoForm(forms.ModelForm):
    estregistro = forms.ChoiceField(
        required=True, label='Estado del registro', choices=ESTREGISTRO_TYPES)

    class Meta:
        model = Departamento
        fields = ['codigo','nombre', 'estregistro']
        labels = {
            'codigo': _('Codigo DANE'),
            'nombre': _('Nombres'), 'estregistro': _('Estado registro'),
        }

class MetodologiaForm(forms.ModelForm):
    estregistro = forms.ChoiceField(
        required=True, label='Estado del registro', choices=ESTREGISTRO_TYPES)

    class Meta:
        model = Metodologia
        fields = ['codigo','nombre', 'estregistro']
        labels = {
            'codigo': _('Id'),
            'nombre': _('Nombre'), 'estregistro': _('Estado registro'),
        }

class EspecialidadForm(forms.ModelForm):
    estregistro = forms.ChoiceField(
        required=True, label='Estado del registro', choices=ESTREGISTRO_TYPES)

    class Meta:
        model = Especialidad
        fields = ['codigo','nombre', 'estregistro']
        labels = {
            'codigo': _('Id'),
            'nombre': _('Nombre'), 'estregistro': _('Estado registro'),
        }
        widgets = {
            'codigo': forms.TextInput({'placeholder': 'Ingrese id'}),
            'nombre': forms.TextInput({'placeholder': 'Ingrese nombre'})
        }