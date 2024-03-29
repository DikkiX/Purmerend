# Generated by Django 4.1.9 on 2023-07-30 19:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("webservice", "0088_rename_layer_id_layer_slug_alter_map_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Drawing",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("features", models.JSONField()),
            ],
            options={
                "verbose_name": "Tekening",
                "verbose_name_plural": "Tekeningen",
            },
        ),
    ]
