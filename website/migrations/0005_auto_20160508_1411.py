# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 12:11
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20160427_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='body_text',
            field=tinymce.models.HTMLField(),
        ),
    ]