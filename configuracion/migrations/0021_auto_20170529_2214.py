# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-30 03:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0020_grados_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grados',
            name='nivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Niveles', related_query_name='Niveles', to='configuracion.Niveles'),
        ),
    ]