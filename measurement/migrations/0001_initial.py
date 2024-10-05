# Generated by Django 5.1.1 on 2024-10-05 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sensor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Measurement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("temperature", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "sensor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="measurements",
                        to="measurement.sensor",
                    ),
                ),
            ],
        ),
    ]
