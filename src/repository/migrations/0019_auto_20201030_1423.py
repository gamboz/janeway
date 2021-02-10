# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-30 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0018_auto_20201027_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='versionqueue',
            name='file',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.PreprintFile'),
        ),
        migrations.AlterField(
            model_name='versionqueue',
            name='update_type',
            field=models.CharField(choices=[('correction', 'Text Correction'), ('metadata_correction', 'Metadata Correction'), ('version', 'New Version')], max_length=20),
        ),
    ]