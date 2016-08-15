# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-24 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CLiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=30)),
                ('Apellido', models.CharField(blank=True, max_length=30)),
                ('Cedula', models.CharField(max_length=10)),
                ('Direccion', models.CharField(blank=True, max_length=30)),
                ('Telefono', models.CharField(blank=True, max_length=10)),
                ('Correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.IntegerField()),
                ('PrecioTotal', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=30)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Descripcion', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=30)),
                ('Gerente', models.CharField(blank=True, max_length=30)),
                ('Direccion', models.CharField(blank=True, max_length=30)),
                ('Telefono', models.CharField(max_length=10)),
            ],
        ),
    ]
