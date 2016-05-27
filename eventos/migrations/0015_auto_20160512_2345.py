# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-13 04:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0014_auto_20160512_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplicant',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Evento'),
        ),
        migrations.AlterField(
            model_name='aplicant',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='aplicantes', to=settings.AUTH_USER_MODEL),
        ),
    ]
