# Generated by Django 4.2 on 2023-05-03 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hos_list",
            name="date",
            field=models.DateField(),
        ),
    ]
