# Generated by Django 3.2.13 on 2022-09-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0068_template_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='fields',
            field=models.TextField(blank=True, help_text='Voer één veld per regel in.', null=True, verbose_name='Tabel velden'),
        ),
        migrations.AlterField(
            model_name='template',
            name='headers',
            field=models.TextField(blank=True, help_text='Voer één veld per regel in.', max_length=128, null=True, verbose_name='Tabel kopjes'),
        ),
        migrations.AlterField(
            model_name='template',
            name='list',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Tabel Veld met lijst'),
        ),
        migrations.AlterField(
            model_name='template',
            name='template',
            field=models.TextField(blank=True, null=True, verbose_name='Vrij veld template'),
        ),
    ]
