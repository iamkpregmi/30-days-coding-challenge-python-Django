# Generated by Django 4.2 on 2023-06-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myfileupload",
            name="myfile",
            field=models.FileField(
                default=None, max_length=200, null=True, upload_to="test/"
            ),
        ),
    ]
