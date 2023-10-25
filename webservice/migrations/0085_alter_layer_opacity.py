# Generated by Django 4.0.1 on 2023-06-01 14:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0084_alter_viewer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='opacity',
            field=models.DecimalField(decimal_places=1, default=0.9, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='Transparantie'),
        ),
    ]