# Generated by Django 3.2.5 on 2021-07-27 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0002_alter_mindpalacenode_body_type'),
        ('stats', '0002_alter_nodelearningstatistics_easiness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodelearningstatistics',
            name='node',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='learning_statistics', to='node.mindpalacenode'),
        ),
    ]