# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-11 02:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0006_tetnias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(error_messages={'invalid': 'Ingreseeeeee un valor valido', 'required': 'Esteeeeeee campo es requerido.'}, max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('numerodocumento', models.CharField(max_length=30, verbose_name='Numero de documento')),
                ('direccion', models.CharField(blank=True, max_length=100, verbose_name='Direccion')),
                ('telefono', models.CharField(blank=True, max_length=50, verbose_name='Telefono')),
                ('fechanacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('correoelectronico', models.EmailField(max_length=254, verbose_name='Correo electronico')),
                ('genero', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Genero de nacimiento')),
                ('estregistro', models.IntegerField(default=1)),
                ('foto', models.ImageField(blank=True, default='fotos/personas/avatars_mini.png', upload_to='fotos/personas/')),
                ('tdocumento', models.ForeignKey(error_messages={'required': 'Please choose a star rating'}, on_delete=django.db.models.deletion.CASCADE, to='administracion.Tdocumento', verbose_name='Tipo de documento')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='persona',
            unique_together=set([('nombres', 'apellidos', 'numerodocumento')]),
        ),
    ]
