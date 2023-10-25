# Generated by Django 2.2 on 2019-04-15 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0008_atlastheme'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atlastheme',
            options={'verbose_name': 'Thema',
                     'verbose_name_plural': "Thema's"},
        ),
        migrations.AddField(
            model_name='layer',
            name='not_in_atlas',
            field=models.BooleanField(default=False, help_text='\nKaartlaag wordt niet in Atlas getoond, alleen als kaartlaag in een thema.\n        ',
                                      verbose_name='Alleen in een thema, niet in Atlas'),
        ),
    ]