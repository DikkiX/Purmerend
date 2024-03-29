# Generated by Django 4.1.9 on 2023-08-31 09:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webservice", "0089_drawing"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="source",
            options={
                "ordering": ["title"],
                "verbose_name": "Bron",
                "verbose_name_plural": "Bronnen",
            },
        ),
        migrations.AlterField(
            model_name="viewer",
            name="internal",
            field=models.BooleanField(
                default=True,
                help_text="Hou er rekening mee dat de gebruikernaam, het wachtwoord of de API key gedeeld wordt met het publieke internet op het moment dat deze optie uit staat.",
                verbose_name="Alleen zichtbaar voor ingelogde gebruikers en interne omgeving",
            ),
        ),
    ]
 