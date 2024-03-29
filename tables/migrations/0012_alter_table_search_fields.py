# Generated by Django 4.1.9 on 2023-10-08 18:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tables", "0011_alter_table_search_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="table",
            name="search_fields",
            field=models.JSONField(
                blank=True,
                default=list,
                verbose_name="Velden waarop gezocht kan worden",
            ),
        ),
    ]
