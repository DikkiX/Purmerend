# Generated by Django 4.1.9 on 2023-07-27 13:03

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ("webservice", "0087_source_slug_alter_category_slug_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="layer",
            old_name="layer_id",
            new_name="slug",
        ),
        migrations.AlterField(
            model_name="map",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                editable=False,
                help_text="Een uniek kort kenmerk voor de kaart in Atlas.",
                populate_from="title",
                unique=True,
                verbose_name="Kort kenmerk",
            ),
        ),
    ]
