# Generated by Django 4.0.1 on 2023-05-11 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0083_layer_is_selectable_alter_layer_show_in_detail_panel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewer',
            name='type',
            field=models.CharField(choices=[('GOOGLE_MAPS', 'Google Maps'), ('STREET_SMART', 'Street Smart'), ('OBLIQUO', 'Obliquo'), ('IFRAME', 'Iframe')], default='GOOGLE_MAPS', max_length=20, verbose_name='Type'),
        ),
    ]