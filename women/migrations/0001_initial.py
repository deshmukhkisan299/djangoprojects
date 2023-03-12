# Generated by Django 4.1.4 on 2023-01-20 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="womenmodel",
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
                ("name", models.CharField(max_length=15)),
                ("age", models.IntegerField()),
                ("city", models.CharField(max_length=15)),
                ("salary", models.IntegerField()),
            ],
        ),
    ]