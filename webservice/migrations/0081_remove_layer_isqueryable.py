# Generated by Django 4.0.1 on 2023-04-19 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0080_layer_friendly_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layer',
            name='isqueryable',
        ),
    ]
