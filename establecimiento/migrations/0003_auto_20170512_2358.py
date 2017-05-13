# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-13 04:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0002_establecimientos_estregistro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establecimientos',
            name='codigo',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.MinLengthValidator(12)]),
        ),
    ]