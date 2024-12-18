# Generated by Django 4.2.16 on 2024-11-30 06:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=255)),
                ("industry", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("revenue", models.FloatField()),
            ],
        ),
    ]
