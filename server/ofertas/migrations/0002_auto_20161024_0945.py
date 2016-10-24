# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='time',
        ),
        migrations.AddField(
            model_name='offer',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='offer',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
