# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 14:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='usuario',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='username',
        ),
    ]
