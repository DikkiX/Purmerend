# Generated by Django 3.2.10 on 2022-03-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0056_alter_layer_opacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='opacity',
            field=models.DecimalField(decimal_places=1, default=0.9, max_digits=1, verbose_name='Transparantie'),
        ),
    ]
