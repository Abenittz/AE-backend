# Generated by Django 4.1.1 on 2023-09-07 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_attendee_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='events',
            field=models.ManyToManyField(
                related_name='attendees_attending', to='api.event'),
        ),
    ]
