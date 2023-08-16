# Generated by Django 3.2.19 on 2023-08-03 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0082_galley_file_not_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='scrubbed',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scrubs', to='core.file'),
        ),
    ]