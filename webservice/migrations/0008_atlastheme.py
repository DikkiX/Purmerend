# Generated by Django 2.2 on 2019-04-12 08:40

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0007_auto_20190409_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtlasTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, null=True, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, overwrite=True, populate_from='title')),
                ('layers', models.ManyToManyField(to='webservice.Layer')),
            ],
        ),
    ]
