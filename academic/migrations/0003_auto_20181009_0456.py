# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-09 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20181005_1102'),
        ('academic', '0002_exam_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_name',
            new_name='course',
        ),
        migrations.AddField(
            model_name='assessment',
            name='attendance',
            field=models.CharField(choices=[('A', 'Absent'), ('P', 'Present')], default='P', editable=False, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessment',
            name='course',
            field=models.ForeignKey(default=None, editable=False, on_delete=django.db.models.deletion.CASCADE, to='academic.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessment',
            name='department',
            field=models.ForeignKey(default=None, editable=False, on_delete=django.db.models.deletion.CASCADE, to='academic.Department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessment',
            name='marks_scored',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessment',
            name='out_of',
            field=models.IntegerField(default=100, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessment',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profiles.Student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessment',
            name='subject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='academic.Subject'),
            preserve_default=False,
        ),
    ]
