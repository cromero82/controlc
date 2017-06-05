# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-30 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0019_auto_20170529_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='grados',
            name='nivel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Niveles', to='configuracion.Niveles'),
            preserve_default=False,
        ),
    ]