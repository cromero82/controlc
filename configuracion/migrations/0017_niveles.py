# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-29 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0016_tfuenterecursos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Niveles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(error_messages={'invalid': 'El valor ingresado no es valido', 'required': 'Este campo es requerido.', 'unique': 'Ya se encuentra registrado en el sistema.'}, max_length=2, unique=True)),
                ('nombre', models.CharField(error_messages={'invalid': 'El valor ingresado no es valido', 'required': 'Este campo es requerido.', 'unique': 'Ya se encuentra registrado en el sistema.'}, max_length=200, unique=True)),
                ('estregistro', models.IntegerField(default=1)),
            ],
            options={
                'default_related_name': 'Niveles',
            },
        ),
    ]
