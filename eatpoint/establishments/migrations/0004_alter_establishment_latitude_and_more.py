# Generated by Django 4.2.5 on 2023-11-15 23:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "establishments",
            "0003_establishment_latitude_establishment_longitude",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="establishment",
            name="latitude",
            field=models.FloatField(
                blank=True, max_length=200, null=True, verbose_name="Широта"
            ),
        ),
        migrations.AlterField(
            model_name="establishment",
            name="longitude",
            field=models.FloatField(
                blank=True, max_length=200, null=True, verbose_name="Долгота"
            ),
        ),
    ]