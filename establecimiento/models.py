from __future__ import unicode_literals
from configuracion.models import Tdocumento
from django.db import models

# Create your models here.
class Establecimientos (models.Model):
    nombre = models.CharField(max_length=200, blank=False)
    codigo = models.CharField(max_length=12,  blank=False, unique=True)
    direccion = models.CharField(max_length=100, blank=False)
    def __unicode__(self):  # __unicode__ en Python 2
        return self.nombre 
    # class Meta:
    #     unique_together = (('codigo'))