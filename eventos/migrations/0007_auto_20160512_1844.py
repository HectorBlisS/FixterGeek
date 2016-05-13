# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0006_evento_boton'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='detalles',
            field=models.CharField(max_length=140),
        ),
    ]