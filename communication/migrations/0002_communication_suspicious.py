# Generated by Django 4.1 on 2022-08-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("communication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="communication",
            name="suspicious",
            field=models.BooleanField(default=False),
        ),
    ]
