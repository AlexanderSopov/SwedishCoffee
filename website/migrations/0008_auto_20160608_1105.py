# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20160608_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='imgUrl',
            field=models.TextField(),
        ),
    ]
