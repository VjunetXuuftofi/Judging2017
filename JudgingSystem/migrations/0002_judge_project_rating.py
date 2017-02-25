# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-24 01:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessions', '0001_initial'),
        ('JudgingSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('session_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sessions.Session')),
                ('submitted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'session',
                'verbose_name_plural': 'sessions',
            },
            bases=('sessions.session',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mean_standardized_score', models.DecimalField(decimal_places=4, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originality', models.IntegerField(null=True)),
                ('usefulness', models.IntegerField(null=True)),
                ('technical_difficulty', models.IntegerField(null=True)),
                ('polish', models.IntegerField(null=True)),
                ('standardized_originality', models.IntegerField(null=True)),
                ('standardized_usefulness', models.IntegerField(null=True)),
                ('standardized_technical_difficulty', models.IntegerField(null=True)),
                ('standardized_polish', models.IntegerField(null=True)),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JudgingSystem.Judge')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JudgingSystem.Project')),
            ],
        ),
    ]