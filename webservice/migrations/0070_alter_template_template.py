# Generated by Django 3.2.13 on 2022-09-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0069_auto_20220929_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='template',
            field=models.TextField(blank=True, help_text='Het is mogelijk om Markdown te gebruiken.', null=True, verbose_name='Vrij veld template'),
        ),
    ]
