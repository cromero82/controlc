# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-17 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0009_auto_20170516_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metodologia',
            name='codigo',
            field=models.CharField(error_messages={'unique': 'Numero de metodologia ya existe.'}, max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='metodologia',
            name='estregistro',
            field=models.IntegerField(default=1, error_messages={'invalid': 'El valor ingresado no es valido', 'required': 'Este campo es requerido.', 'unique': 'Ya se encuentra registrado en el sistema.'}),
        ),
        migrations.AlterField(
            model_name='metodologia',
            name='nombre',
            field=models.CharField(error_messages={'invalid': 'El valor ingresado no es valido', 'required': 'Este campo es requerido.', 'unique': 'Ya se encuentra registrado en el sistema.'}, max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='municipios',
            name='codigo',
            field=models.CharField(error_messages={'invalid': 'El valor ingresado no es valido', 'required': 'Este campo es requerido.', 'unique': 'Ya se encuentra registrado en el sistema.'}, max_length=3),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombres',
            field=models.CharField(error_messages={'invalid': 'El valor ingresado no es valido', 'required': 'Este campo es requerido.', 'unique': 'Ya se encuentra registrado en el sistema.'}, max_length=50, verbose_name='Nombres'),
        ),
    ]