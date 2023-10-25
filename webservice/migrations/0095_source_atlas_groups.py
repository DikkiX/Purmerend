# Generated by Django 4.1.9 on 2023-09-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_management", "0004_alter_atlasuser_first_name"),
        ("webservice", "0094_source_login_required"),
    ]

    operations = [
        migrations.AddField(
            model_name="source",
            name="atlas_groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="De inhoud van deze dataset kan alleen bekeken worden als de gebruiker lid is van een van deze groepen.",
                to="user_management.atlasgroup",
                verbose_name="Groepen",
            ),
        ),
    ]
