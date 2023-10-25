# Generated by Django 3.2.13 on 2022-10-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0072_source_authenticate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='authenticate',
            field=models.BooleanField(default=False, help_text='Configureer dit alleen voor vertrouwde bronnen',
                                      verbose_name='Verstuur authenticatieinformatie naar bron'),
        ),
    ]