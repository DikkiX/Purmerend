# Generated by Django 4.1.9 on 2023-09-20 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_management", "0005_atlasgroup_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="atlasgroup",
            name="external_id",
            field=models.CharField(
                blank=True,
                editable=False,
                max_length=255,
                null=True,
                verbose_name="External ID",
            ),
        ),
        migrations.AddField(
            model_name="atlasuser",
            name="external_id",
            field=models.CharField(
                blank=True,
                editable=False,
                max_length=255,
                null=True,
                verbose_name="External ID",
            ),
        ),
    ]