# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20160508_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='body_text',
            field=models.TextField(),
        ),
    ]