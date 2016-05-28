from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Estregistro(models.Model):
	nombre  = models.CharField(max_length = 10, default='normal')

class Tdocumentos(models.Model):
	nombre = models.CharField(max_length=50)
	sigla = models.CharField(max_length=5)
	estadoregistro = models.ForeignKey(Estregistro, related_name='Estado')

class Departamentos (models.Model):
	nombre= models.CharField(max_length=50)

class Municipios (models.Model):
	departamento = models.ForeignKey(Departamentos, related_name='Departamento')
	nombre= models.CharField(max_length=50)