# Generated by Django 4.1.5 on 2023-01-12 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("signup", "0003_alter_signup_model_gender"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="signup_model",
            name="gender",
        ),
    ]
