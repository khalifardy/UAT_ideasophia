# Generated by Django 4.2.3 on 2023-08-24 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("akasia", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
    ]
