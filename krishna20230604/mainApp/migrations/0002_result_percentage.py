# Generated by Django 4.2 on 2023-06-04 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="result",
            name="Percentage",
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
    ]
