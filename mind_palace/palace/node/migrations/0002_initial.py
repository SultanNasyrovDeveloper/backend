# Generated by Django 4.0.5 on 2022-07-20 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('node', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='palacenode',
            name='owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nodes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='palacenode',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='node.palacenode', verbose_name='Parent'),
        ),
        migrations.AddField(
            model_name='palacenode',
            name='tags',
            field=models.ManyToManyField(to='node.tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='media',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='node.palacenode'),
        ),
        migrations.AddField(
            model_name='body',
            name='node',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='body', to='node.palacenode'),
        ),
    ]
