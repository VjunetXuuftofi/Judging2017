# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-25 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JudgingSystem', '0003_auto_20170224_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='passed',
            field=models.BooleanField(default=False),
        ),
    ]
