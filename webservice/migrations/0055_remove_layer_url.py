# Generated by Django 3.2.10 on 2022-02-03 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0054_move_url_to_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layer',
            name='url',
        ),
    ]
