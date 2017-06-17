from __future__ import unicode_literals

from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
my_default_errors = {
    'required': 'Este campo es requerido.',
    'invalid': 'El valor ingresado no es valido',
    'unique':"Ya se encuentra registrado en el sistema."
}

class Tactoadmin(models.Model):    
    aplicacion = models.CharField(max_length=3, blank=False, error_messages=my_default_errors)
    nombre = models.CharField(max_length=200, blank=False, unique=True, error_messages=my_default_errors)
    estregistro = models.IntegerField(default=1, blank=False)
    class Meta:
        default_related_name = 'Tactoadmin'
    def __unicode__(self):  
        return self.nombre
    def natural_key(self):
        return self.nombre

class Niveles(models.Model):    
    codigo = models.CharField(max_length=2, blank=False,  unique=True, error_messages=my_default_errors)
    nombre = models.CharField(max_length=200, blank=False, unique=True, error_messages=my_default_errors)
    estregistro = models.IntegerField(default=1, blank=False)
    class Meta:
        default_related_name = 'Niveles'
    def __unicode__(self):  
        return self.nombre
    def natural_key(self):
        return self.nombre

class Grados(models.Model):
    nivel = models.ForeignKey(Niveles, related_query_name='Niveles')
    codigo = models.IntegerField( blank=False,  unique=True, validators=[MinValueValidator(-3),
                                       MaxValueValidator(100)], error_messages=my_default_errors)
    nombre = models.CharField(max_length=200, blank=False, unique=True, error_messages=my_default_errors)
    estregistro = models.IntegerField(default=1, blank=False)
    class Meta:
        default_related_name = 'Grados'
    def __unicode__(self):  
        return self.nombre  

class TfuenteRecursos(models.Model):
    codigo = models.CharField(max_length=2, blank=False,  unique=True, error_messages=my_default_errors)
    nombre = models.CharField(max_length=200, blank=False, unique=True, error_messages=my_default_errors)
    estregistro = models.IntegerField(default=1, blank=False)
    class Meta:
        default_related_name = 'Tfuenterecursos'
    def __unicode__(self):  
        return self.nombre

class Tcaracter(models.Model):
    codigo = models.CharField(max_length=2, blank=False,  unique=True, error_messages=my_default_errors)
    nombre = models.CharField(max_length=200, blank=False, unique=True, error_messages=my_default_errors)
    estregistro = models.IntegerField(default=1, blank=False)
    class Meta:
        default_related_name = 'Tcaracter'
    def __unicode__(self):  
        return self.nombre

class Tjornada(models.Model):
    codigo = models.CharField(max_length=2, blank=False,  unique=True, error_messages=my_default_errors)
    nombre = models.CharField(max_length=40, blank=False, unique=True, error_messages=my_default_errors)
    estregistro = models.IntegerField(default=1, blank=False)
    class Meta:
        default_related_name = 'Tjornada'
    def __unicode__(self):  
        return self.nombre
    def natural_key(self):
        return self.nombre

class Especialidad(models.Model):
    codigo = models.CharField(max_length=2, blank=False,  unique=True, error_messages=my_default_errors)
    nombre = models.CharField(max_length=40, blank=False, unique=True, error_messages=my_default_errors)
    estregistro = models.IntegerField(default=1, blank=False)
    class Meta:
        default_related_name = 'nombre'
    def __unicode__(self):  
        return self.nombre

class Metodologia(models.Model):
    codigo = models.CharField(max_length=2, blank=False,  unique=True, error_messages=my_default_errors)
    nombre = models.CharField(max_length=40, blank=False, unique=True, error_messages=my_default_errors)
    estregistro = models.IntegerField(default=1, blank=False, error_messages=my_default_errors)
    class Meta:
        default_related_name = 'metodologia'
    def __unicode__(self):  
        return self.nombre

class Estregistro(models.Model):
    nombre = models.CharField(max_length=10, default='normal')    
    def __unicode__(self):  # __unicode__ en Python 2
        return self.nombre

class Tdocumento(models.Model):
    nombre = models.CharField(max_length=50)
    sigla = models.CharField(max_length=8)
    estregistro = models.IntegerField(default=1, blank=False)
    def __unicode__(self):  # __unicode__ en Python 2
        return self.nombre

class Persona (models.Model):
    nombres = models.CharField(max_length=50, verbose_name='Nombres', blank=False, error_messages = my_default_errors)
    apellidos = models.CharField(max_length=50, verbose_name='Apellidos', blank=False)
    numerodocumento = models.CharField(max_length=30, verbose_name='Numero de documento', blank=False)
    tdocumento = models.ForeignKey(Tdocumento, verbose_name='Tipo de documento', blank=False,  error_messages={'required': 'Please choose a star rating'})
    direccion = models.CharField(max_length=100, blank=True, verbose_name='Direccion')
    telefono = models.CharField(max_length=50, blank=True, verbose_name='Telefono')
    fechanacimiento = models.DateField(verbose_name='Fecha de nacimiento', blank=False)
    correoelectronico = models.EmailField(verbose_name='Correo electronico', blank=False)
    genero = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino')), verbose_name='Genero de nacimiento', blank=True)
    estregistro = models.IntegerField(default=1, blank=False)
    foto = models.ImageField(upload_to='fotos/personas/', default='fotos/personas/avatars_mini.png', blank=True)
    def __unicode__(self):  # __unicode__ en Python 2
        return self.nombres + " " + self.apellidos
    class Meta:
        unique_together = (('nombres', 'apellidos', 'numerodocumento'))

class TEtnias (models.Model):
    nombre = models.CharField(max_length=50)
    sigla = models.CharField(max_length=8)
    estregistro = models.IntegerField(default=1, blank=False)
    def __unicode__(self):  # __unicode__ en Python 2
        return self.nombre



class TRelacionFamiliar(models.Model):
    nombre = models.CharField(max_length=50,  blank=False)
    estregistro = models.IntegerField(default=1, blank=False)

class Departamento (models.Model):
    codigo = models.CharField(max_length=2, blank=True, unique=True)
    nombre = models.CharField(max_length=50, blank=False)
    estregistro = models.IntegerField(blank=False, default=1)
    def __unicode__(self):  # __unicode__ en Python 2
        return self.nombre
    def natural_key(self):
        return self.nombre
    class Meta:
        unique_together = (('codigo', 'nombre'))

class Municipios(models.Model):
    codigo = models.CharField(max_length=3, blank=False, error_messages = my_default_errors)
    nombre = models.CharField(max_length=50,  blank=False)
    estregistro = models.IntegerField(default=1, blank=False)
    departamento = models.ForeignKey(Departamento, related_query_name='Departamento')
    def __unicode__(self):  # __unicode__ en Python 2
        return self.nombre
    def natural_key(self):
        return self.nombre
    class Meta:
        unique_together = (('codigo', 'departamento'))
