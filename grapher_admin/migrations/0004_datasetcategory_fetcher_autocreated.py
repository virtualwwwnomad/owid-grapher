# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-08 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grapher_admin', '0003_auto_20170602_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetcategory',
            name='fetcher_autocreated',
            field=models.BooleanField(default=False),
        ),
    ]
