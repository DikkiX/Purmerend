# Generated by Django 3.2.7 on 2021-10-14 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0039_alter_layer_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='source_type',
            field=models.CharField(choices=[('WMS_WFS', 'WMS en WFS'), ('WMS', 'WMS'), ('WFS', 'WFS'), ('WMTS', 'WMTS'), ('MVT', 'MVT')], default='WMS_WFS',
                                   help_text='"WMS en WFS" en WFS is zichtbaar in zowel het datapaneel als op de kaart. WMS en WMTS toont alleen op de kaart.', max_length=20, verbose_name='Brontype'),
        ),
    ]
