# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-02-17 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0065_auto_20211221_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ISSN_override',
            field=models.CharField(blank=True, help_text="Original ISSN of this article's journal when published Only relevant for back content published under a different title", max_length=999, null=True),
        ),
    ]
