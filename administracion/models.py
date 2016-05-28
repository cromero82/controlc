from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Estregistro(models.Model):
	nombre  = models.CharField(max_length = 10, default='normal')
	def __unicode__(self): # __unicode__ en Python 2
		return	self.nombre

class Tdocumento(models.Model):
	nombre = models.CharField(max_length=50)
	sigla = models.CharField(max_length=5)
	estadoregistro = models.ForeignKey(Estregistro, related_name='Estado')
	def __unicode__(self): # __unicode__ en Python 2
		return	self.nombre

class Departamento (models.Model):
	nombre= models.CharField(max_length=50)
	def __unicode__(self): # __unicode__ en Python 2
		return	self.nombre

class Municipio (models.Model):
	departamento = models.ForeignKey(Departamento, related_name='Departamento')
	nombre= models.CharField(max_length=50)
	def __unicode__(self): # __unicode__ en Python 2
		return	self.nombre