# Generated by Django 2.2 on 2019-04-09 12:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_management', '0001_initial'),
        ('webservice', '0006_auto_20190409_1417'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ThemeLayer',
            new_name='Layer',
        ),
    ]