# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20160427_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='imgUrl',
            field=models.TextField(),
        ),
    ]