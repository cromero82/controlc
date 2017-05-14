from django import forms
from models import Establecimientos
from django.utils.translation import gettext_lazy as _
from django.forms import Field
from django.utils.translation import ugettext

class EstablecimientoForm(forms.ModelForm):
    class Meta:
        model = Establecimientos
        fields = ['id', 'nombre', 'codigo', 'direccion']
        labels = {'nombre': _('Nombre'), 'codigo': _(
            'Codigo DANE'), 'direccion': _('Direccion')}
