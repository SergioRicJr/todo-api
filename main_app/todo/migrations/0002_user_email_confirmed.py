# Generated by Django 4.2.7 on 2024-01-08 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="email_confirmed",
            field=models.BooleanField(default=False),
        ),
    ]