# Generated by Django 4.1.1 on 2023-10-29 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_delete_appuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_status',
        ),
    ]
