# Generated by Django 5.0.4 on 2024-08-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_itinerary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='weather_data',
            field=models.JSONField(),
        ),
    ]
