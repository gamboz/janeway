# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-15 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0014_auto_20210414_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='decisiondraft',
            name='editor_decline_rationale',
            field=models.TextField(blank=True, help_text='Provide the section editor with a rationale for declining their drafted decision.', null=True, verbose_name='Rationale for Declining Draft Decision'),
        ),
    ]