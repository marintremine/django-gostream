# Generated by Django 4.1 on 2023-04-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipe', '0005_equipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='streamer',
            name='color',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='streamer',
            name='discord',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='streamer',
            name='pourcent1',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='streamer',
            name='pourcent2',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='streamer',
            name='pourcent3',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='streamer',
            name='skill1',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='streamer',
            name='skill2',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='streamer',
            name='skill3',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
