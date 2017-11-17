# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 21:30
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='hashes',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='source',
            field=models.ImageField(max_length=500, upload_to='images'),
        ),
    ]