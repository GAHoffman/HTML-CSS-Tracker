# Generated by Django 4.1.5 on 2023-01-31 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="description",
            field=models.TextField(default="Please describe"),
            preserve_default=False,
        ),
    ]
