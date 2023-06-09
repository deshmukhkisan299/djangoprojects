# Generated by Django 4.1.5 on 2023-01-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("signup", "0002_signup_model_delete_signup_form_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signup_model",
            name="gender",
            field=models.CharField(
                choices=[("Male", "male"), ("Female", "female"), ("Others", "others")],
                default="male",
                max_length=7,
            ),
        ),
    ]
