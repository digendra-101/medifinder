# Generated by Django 4.2 on 2023-05-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0004_alter_hos_list_desc_alter_hos_list_services"),
    ]

    operations = [
        migrations.AddField(
            model_name="hos_list",
            name="contact",
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]
