from __future__ import unicode_literals

from configuracion.models import Tdocumento, Municipios, Tjornada
from django.db import models
from django.core.validators import MinLengthValidator
from datetime import date

# Create your models here.
class Establecimientos (models.Model):
    nombre = models.CharField(unique=True, max_length=200, blank=False)
    nombreRector = models.CharField(max_length=200, blank=False, default='Rector de prueba')
    codigo = models.CharField(unique=True,  max_length=12, validators=[MinLengthValidator(12)], blank=False)        
    fechafundacion = models.DateField(verbose_name='Fecha de fundacion', blank=False, default=date.today)
    numsedes = models.IntegerField(default=1, blank=True)
    tieneMatriculaContrada = models.CharField(max_length=1, choices=(('S', 'Si'), ('N', 'No')), verbose_name='tiene matricula contratada', blank=True)
    #caracter    
    #tipoPropietario #OFICIAL, PERSONA NATURAL (FALTA TIPO DE PRESTADOR DE SERVICIO)
    # calendario # A - B - OTRO
    municipio = models.ForeignKey(Municipios, related_query_name='Municipio', default= 1)
    escudo = models.ImageField(upload_to='institucional/', default='institucional/escudo_defecto2.png', blank=False)
    estregistro = models.IntegerField(default=1, blank=False)
    def __unicode__(self):  # __unicode__ en Python 2
        return self.nombre 
    def natural_key(self):
        return self.nombre

class Sedes (models.Model):
    establecimiento = models.ForeignKey(Establecimientos, related_query_name='Establecimiento', default= 1)
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=2, validators=[MinLengthValidator(2)], blank=False)
    correoelectronico = models.EmailField(unique=True, verbose_name='Correo electronico', blank=True)
    direccion = models.CharField(max_length=100, blank=True, verbose_name='Direccion')
    telefono = models.CharField(max_length=50, blank=True, verbose_name='Telefono')
    responsable = models.CharField(max_length=200, blank=False, default='Persona prueba')
    estregistro = models.IntegerField(default=1, blank=False)
    class Meta:
        unique_together = (('establecimiento', 'codigo'))
    def __unicode__(self):  # __unicode__ en Python 2
        return self.nombre
    def natural_key(self):
        return self.nombre

class Jornadas (models.Model):
    sede = models.ForeignKey(Sedes, related_query_name='Sede')
    jornada = models.ForeignKey(Tjornada, related_query_name='Tjornada')
    estregistro = models.IntegerField(default=1, blank=False)
    class Meta:
        unique_together = (('sede', 'jornada'))
    # def __unicode__(self):  # __unicode__ en Python 2
    #     return self.nombre
    # def natural_key(self):
    #     return self.nombre