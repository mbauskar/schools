# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-09 05:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_auto_20181009_0546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='subject',
        ),
    ]
