# -*- coding: utf-8 -*-
# Generated by Django 1.9.dev20150902175238 on 2015-09-07 23:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloak', '0003_auto_20150907_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='obfuscated_url',
            new_name='obfuscated_key',
        ),
    ]
