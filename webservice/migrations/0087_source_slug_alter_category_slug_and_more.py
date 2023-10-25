# Generated by Django 4.1.9 on 2023-07-27 12:55

from django.db import migrations, models
import django_extensions.db.fields


def add_slug_to_source(apps, _):
    Source = apps.get_model('webservice', 'source')

    for source in Source.objects.all():
        source.save()


class Migration(migrations.Migration):
    dependencies = [
        ("webservice", "0086_remove_layer_style_layer_client_style_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="source",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                default=None,
                editable=False,
                help_text="Een uniek kort kenmerk voor de bron in Atlas.",
                null=True,
                populate_from="title",
                unique=True,
                verbose_name="Kort kenmerk",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                editable=False,
                help_text="Een uniek kort kenmerk voor de categorie in Atlas.",
                populate_from="title",
                unique=True,
                verbose_name="Kort kenmerk",
            ),
        ),
        migrations.AlterField(
            model_name="layer",
            name="client_style",
            field=models.JSONField(
                blank=True,
                default=dict,
                help_text="Stijl in GeoStyler formaat",
                null=True,
                verbose_name="Stijl voor WFS / MVT laag",
            ),
        ),
        migrations.AlterField(
            model_name="map",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                editable=False,
                help_text="Een uniek kort kenmerk voor de kaart in Atlas. Dit kenmerk komt terug in links naar het thema.",
                populate_from="title",
                unique=True,
                verbose_name="Kort kenmerk",
            ),
        ),
        migrations.RunPython(add_slug_to_source, migrations.RunPython.noop),
    ]
