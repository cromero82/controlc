# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-31 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0004_auto_20170528_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='establecimientos',
            name='escudo',
            field=models.ImageField(default='institucional/escudo_defecto2.png', upload_to='institucional/'),
        ),
    ]
