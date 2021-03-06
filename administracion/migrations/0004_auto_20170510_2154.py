# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-11 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_auto_20170510_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(error_messages={'invalid': 'Ingreseeeeee un valor valido', 'required': 'Esteeeeeee campo es requerido.'}, max_length=3)),
                ('nombre', models.CharField(max_length=50)),
                ('estregistro', models.IntegerField(default=1)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='Departamento', to='administracion.Departamento')),
            ],
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='departamento',
        ),
        migrations.DeleteModel(
            name='Municipio',
        ),
        migrations.AlterUniqueTogether(
            name='municipios',
            unique_together=set([('codigo', 'departamento')]),
        ),
    ]
