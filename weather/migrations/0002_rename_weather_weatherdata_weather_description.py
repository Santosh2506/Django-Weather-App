# Generated by Django 5.1.5 on 2025-02-09 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weatherdata',
            old_name='weather',
            new_name='weather_description',
        ),
    ]
