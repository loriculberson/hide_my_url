# -*- coding: utf-8 -*-
# Generated by Django 1.9.dev20150902175238 on 2015-09-06 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloak', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='obfuscated_url_click_counter',
            field=models.IntegerField(default=0),
        ),
    ]
