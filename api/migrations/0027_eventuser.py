# Generated by Django 5.0.1 on 2024-04-17 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_remove_attendee_the_event_remove_schedule_the_event_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
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
    ]