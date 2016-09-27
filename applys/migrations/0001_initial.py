# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-27 04:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eventos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivos', models.TextField()),
                ('beca', models.BooleanField(choices=[(True, 'Si la necesito'), (False, 'No, que la aproveche alguien más')], default=False)),
                ('tipo', models.CharField(blank=True, choices=[('Beca 20%', 'Beca 20%'), ('Beca 50%', 'Beca 50%')], default='Beca 20%', max_length=50, null=True)),
                ('porque', models.TextField(blank=True, null=True)),
                ('tel', models.CharField(max_length=50)),
                ('tel2', models.CharField(blank=True, max_length=50, null=True)),
                ('path', models.CharField(blank=True, choices=[('backend path', 'Backend Path'), ('videogames path', 'VideoGames Path'), ('mobileapps / sabatino', 'Mobileapps / Sabatino')], default='Backend Path', max_length=140, null=True)),
                ('fecha', models.DateTimeField(auto_now=True, null=True)),
                ('notas', models.CharField(blank=True, max_length=500, null=True)),
                ('pago', models.NullBooleanField(default=False)),
                ('inscrito', models.NullBooleanField(default=False)),
                ('contactado', models.BooleanField(default=False)),
                ('fecha_de_contacto', models.DateTimeField(blank=True, null=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applys', to='eventos.Evento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applys', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
