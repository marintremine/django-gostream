# Generated by Django 4.1 on 2024-08-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partenaire', '0003_partenaire_discord_partenaire_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partenaire',
            name='facebook',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]