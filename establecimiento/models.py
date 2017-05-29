from __future__ import unicode_literals

from configuracion.models import Tdocumento, Municipios
from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Establecimientos (models.Model):
    nombre = models.CharField(unique=True, max_length=200, blank=False)
    nombreRector = models.CharField(max_length=200, blank=False)
    codigo = models.CharField(unique=True,  max_length=12, validators=[MinLengthValidator(12)], blank=False)
    direccion = models.CharField(max_length=100, blank=True, verbose_name='Direccion')
    telefono = models.CharField(max_length=50, blank=True, verbose_name='Telefono')
    fechafundacion = models.DateField(verbose_name='Fecha de fundacion', blank=False)
    numsedes = models.IntegerField(default=1, blank=False)
    tieneMatriculaContrada = models.CharField(max_length=1, choices=(('S', 'Si'), ('N', 'No')), verbose_name='tiene matricula contratada', blank=True)
    #caracter    
    #tipoPropietario #OFICIAL, PERSONA NATURAL (FALTA TIPO DE PRESTADOR DE SERVICIO)
    correoelectronico = models.EmailField(unique=True, verbose_name='Correo electronico', blank=False)
    # calendario # A - B - OTRO
    municipio = models.ForeignKey(Municipios, related_query_name='Municipio')
    estregistro = models.IntegerField(default=1, blank=False)
    def __unicode__(self):  # __unicode__ en Python 2
        return self.nombre 
    # class Meta:
    #     unique_together = (('codigo'))