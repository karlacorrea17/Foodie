# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-23 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfoodie', '0027_auto_20160812_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='contra',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
