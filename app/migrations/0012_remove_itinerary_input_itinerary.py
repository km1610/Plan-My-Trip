# Generated by Django 5.0.4 on 2024-08-26 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_itinerary_weather_data_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itinerary_input',
            name='itinerary',
        ),
    ]