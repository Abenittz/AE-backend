# Generated by Django 5.0.1 on 2024-04-26 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RoomId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomId', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('activity', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('organization', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EventUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_groups', related_query_name='customuser_group', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_permissions', related_query_name='customuser_permission', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'event_users',
                'permissions': (('view_user', 'Can view user'), ('add_speaker', 'Can add speaker'), ('add_sponsor', 'Can add sponsor'), ('change_event', 'Can edit event'), ('delete_event', 'Can delete event'), ('change_user', 'Can edit user'), ('delete_user', 'Can delete user'), ('add_admin', 'Can add admin')),
                'default_related_name': 'event_user',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('registration_start_date', models.DateTimeField()),
                ('registration_end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('available_seat', models.IntegerField()),
                ('attendees', models.ManyToManyField(blank=True, related_name='events_attending', to='api.attendee')),
                ('roomids', models.ManyToManyField(blank=True, related_name='events_roomid', to='api.roomid')),
                ('schedules', models.ManyToManyField(blank=True, related_name='events_scheduled', to='api.schedule')),
                ('speakers', models.ManyToManyField(blank=True, related_name='events_speaking', to='api.speaker')),
                ('sponsors', models.ManyToManyField(blank=True, related_name='events_sponsor', to='api.sponsor')),
            ],
        ),
    ]
