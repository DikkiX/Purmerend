# Generated by Django 2.2 on 2019-11-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0009_auto_20190415_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='js_type',
            field=models.CharField(default='themelayer:true', help_text='javascript...', max_length=64, verbose_name='Javascript type'),
        ),
    ]