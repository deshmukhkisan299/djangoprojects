# Generated by Django 4.1.5 on 2023-01-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("men", "0003_alter_menmodel_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menmodel",
            name="img",
            field=models.ImageField(default=None, upload_to="static/media/"),
        ),
    ]