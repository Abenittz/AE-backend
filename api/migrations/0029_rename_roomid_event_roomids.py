# Generated by Django 5.0.1 on 2024-04-19 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_roomid_event_roomid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='roomid',
            new_name='roomids',
        ),
    ]