# Generated by Django 4.1 on 2022-08-22 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Streamers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('twitch', models.CharField(blank=True, max_length=256)),
                ('twitter', models.CharField(blank=True, max_length=256)),
                ('instagram', models.CharField(blank=True, max_length=256)),
                ('tiktok', models.CharField(blank=True, max_length=256)),
                ('others', models.CharField(blank=True, max_length=256)),
                ('pp', models.ImageField(blank=True, null=True, upload_to='streamers')),
            ],
        ),
    ]