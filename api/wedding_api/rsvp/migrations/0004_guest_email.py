# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0003_auto_20160317_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]