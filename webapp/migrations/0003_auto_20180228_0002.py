# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-28 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_shikigami'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shikigami',
            name='image',
            field=models.ImageField(upload_to='static/webapp/images'),
        ),
    ]
