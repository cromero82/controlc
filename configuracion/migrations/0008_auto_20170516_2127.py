# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-17 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0007_auto_20170515_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metodologia',
            name='codigo',
            field=models.CharField(max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='metodologia',
            name='nombre',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]