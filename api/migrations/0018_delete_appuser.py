# Generated by Django 4.1.1 on 2023-10-27 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_appuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AppUser',
        ),
    ]
