# Generated by Django 2.2.24 on 2021-06-10 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0026_auto_20210610_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='closed_theme',
        ),
    ]