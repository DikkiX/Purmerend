# Generated by Django 2.1.4 on 2019-01-08 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0002_auto_20181127_0815'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theme',
            options={'verbose_name': 'Thema', 'verbose_name_plural': "Thema's"},
        ),
        migrations.AlterModelOptions(
            name='themelayer',
            options={'ordering': ['ordering'], 'verbose_name': 'Thema kaart', 'verbose_name_plural': 'Thema kaarten'},
        ),
        migrations.RemoveField(
            model_name='theme',
            name='the_order',
        ),
        migrations.AddField(
            model_name='themelayer',
            name='ordering',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
