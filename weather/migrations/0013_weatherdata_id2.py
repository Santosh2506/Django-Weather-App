# Generated by Django 5.1.5 on 2025-02-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0012_alter_weatherdata_city_alter_weatherdata_temperature_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherdata',
            name='id2',
            field=models.IntegerField(db_column='id2', default=0),
            preserve_default=False,
        ),
    ]
