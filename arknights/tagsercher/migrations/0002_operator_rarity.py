# Generated by Django 5.2 on 2025-04-29 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagsercher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='rarity',
            field=models.IntegerField(default=3),
        ),
    ]
