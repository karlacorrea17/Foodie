# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-08 01:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appfoodie', '0008_auto_20160724_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurante',
            old_name='idRest',
            new_name='idPro',
        ),
    ]