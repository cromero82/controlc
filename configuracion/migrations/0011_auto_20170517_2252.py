# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-18 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0010_auto_20170517_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialidad',
            name='codigo',
            field=models.CharField(error_messages={'invalid': 'El valor ingresado no es valido', 'required': 'Este campo es requerido.', 'unique': 'Ya se encuentra registrado en el sistema.'}, max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='nombre',
            field=models.CharField(error_messages={'invalid': 'El valor ingresado no es valido', 'required': 'Este campo es requerido.', 'unique': 'Ya se encuentra registrado en el sistema.'}, max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='metodologia',
            name='codigo',
            field=models.CharField(error_messages={'invalid': 'El valor ingresado no es valido', 'required': 'Este campo es requerido.', 'unique': 'Ya se encuentra registrado en el sistema.'}, max_length=2, unique=True),
        ),
    ]
