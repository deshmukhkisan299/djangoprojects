# Generated by Django 4.1.5 on 2023-01-30 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("men", "0002_menmodel_img_alter_menmodel_age_alter_menmodel_city_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menmodel",
            name="img",
            field=models.FileField(default=None, upload_to="static/media/"),
        ),
    ]
