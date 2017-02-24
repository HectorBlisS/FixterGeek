# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-12-31 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='path',
            field=models.CharField(blank=True, choices=[('servers / Semanal', 'Backend & Servers / Semanal'), ('desarrollo_web / Semanal', 'Desarrollo Web / Semanal'), ('desarrollo_web / Sabatino', 'Desarrollo Web  / Sabatino'), ('intro_al_codigo / Semanal', 'Intro al código / Semanal'), ('intro_al_codigo / Sabatino', 'Intro al código / Sabatino')], default='Backend Path', max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='apply',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Beca 20%', 'Beca 20%'), ('Beca 50%', 'Beca 50%'), ('Beca 70%', 'Beca 70%'), ('Beca 80%', 'Beca 80%'), ('Beca 99%', 'Beca 99%')], default='Beca 20%', max_length=50, null=True),
        ),
    ]