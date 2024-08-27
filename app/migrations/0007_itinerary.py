# Generated by Django 5.0.4 on 2024-08-26 14:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_itinerary_input_preferences_delete_choices_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('input_id', models.UUIDField()),
                ('username', models.CharField(max_length=50)),
                ('itinerary', models.TextField()),
                ('weather_data', models.TextField()),
            ],
        ),
    ]
