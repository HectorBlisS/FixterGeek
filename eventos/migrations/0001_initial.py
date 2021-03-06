# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-27 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('slug', models.SlugField(max_length=60)),
                ('descripcion', models.TextField()),
                ('detalles', models.CharField(max_length=140)),
                ('precio', models.CharField(max_length=50)),
                ('precio_promo', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('direccion', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('portada', models.ImageField(blank=True, null=True, upload_to='eventos')),
                ('boton', models.CharField(blank=True, max_length=50, null=True)),
                ('video', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
