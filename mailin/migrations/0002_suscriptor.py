# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-06 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suscriptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=140)),
                ('email', models.CharField(max_length=140)),
            ],
        ),
    ]
