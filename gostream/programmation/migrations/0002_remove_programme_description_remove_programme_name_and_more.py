# Generated by Django 4.1 on 2024-01-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programmation", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="programme",
            name="description",
        ),
        migrations.RemoveField(
            model_name="programme",
            name="name",
        ),
        migrations.RemoveField(
            model_name="programme",
            name="pp",
        ),
        migrations.AddField(
            model_name="programme",
            name="image",
            field=models.ImageField(blank=True, upload_to="programme"),
        ),
    ]