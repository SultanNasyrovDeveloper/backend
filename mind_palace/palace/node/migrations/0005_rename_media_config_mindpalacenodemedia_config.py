# Generated by Django 3.2.5 on 2021-12-12 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0004_auto_20211212_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mindpalacenodemedia',
            old_name='media_config',
            new_name='config',
        ),
    ]
