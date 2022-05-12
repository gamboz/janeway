# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-05-12 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identifiers', '0007_batch_doi_registration_20220315'),
    ]

    operations = [
        migrations.AddField(
            model_name='crossrefdeposit',
            name='status',
            field=models.CharField(blank=True, choices=[('doi', 'DOI'), ('uri', 'URI Path'), ('pubid', 'Publisher ID')], default='Unknown', help_text='A user-friendly message about the status of registration with Crossref.', max_length=255),
        ),
    ]