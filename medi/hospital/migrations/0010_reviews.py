# Generated by Django 4.2 on 2023-05-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0009_alter_hos_list_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="reviews",
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
                ("reviews", models.CharField(max_length=300)),
            ],
        ),
    ]