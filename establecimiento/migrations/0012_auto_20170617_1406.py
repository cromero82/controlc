# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-17 19:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0011_auto_20170609_2238'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='nivelesaprobados',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='nivelesaprobados',
            name='establecimiento',
        ),
        migrations.RemoveField(
            model_name='nivelesaprobados',
            name='nivel',
        ),
        migrations.RemoveField(
            model_name='nivelesaprobados',
            name='tipoaprobacion',
        ),
        migrations.DeleteModel(
            name='Nivelesaprobados',
        ),
    ]
