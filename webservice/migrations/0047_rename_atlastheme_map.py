# Generated by Django 3.2.10 on 2022-02-03 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0046_alter_layer_source_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AtlasTheme',
            new_name='Map',
        ),
    ]
