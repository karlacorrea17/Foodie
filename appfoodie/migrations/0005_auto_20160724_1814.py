# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-24 18:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appfoodie', '0004_auto_20160724_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='idPedi',
        ),
        migrations.RemoveField(
            model_name='restaurante',
            name='idRest',
        ),
    ]
