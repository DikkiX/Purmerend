# Generated by Django 3.2.13 on 2022-05-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0063_alter_layer_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='format',
            field=models.CharField(choices=[('image/png', 'image/png'), ('image/jpeg', 'image/jpeg'), (
                'image/vnd.jpeg-png', 'image/vnd.jpeg-png')], default='image/png', max_length=128, verbose_name='Formaat'),
        ),
    ]