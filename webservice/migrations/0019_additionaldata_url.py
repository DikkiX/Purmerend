# Generated by Django 2.2.17 on 2021-01-27 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0018_auto_20210127_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionaldata',
            name='url',
            field=models.CharField(default='https://datalab.purmerend.nl/geoserver/topp/wms?', max_length=500, verbose_name='URL'),
        ),
    ]
