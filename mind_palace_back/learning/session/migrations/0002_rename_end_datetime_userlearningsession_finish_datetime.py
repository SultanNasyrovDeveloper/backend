# Generated by Django 3.2.5 on 2021-07-19 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlearningsession',
            old_name='end_datetime',
            new_name='finish_datetime',
        ),
    ]
