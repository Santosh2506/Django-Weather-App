from django.db import models

# Create your models here.
from django.db import models

class WeatherData(models.Model):
    city_id = models.IntegerField(default=0,db_column="city_id")
    city = models.CharField(max_length=255, db_column="city")  # Maps to city column
    temperature = models.FloatField(db_column="temperature")  # Maps to temperature column
    weather_description = models.CharField(max_length=255, db_column="weather_description")  # Maps to weather_description

    class Meta:     
        db_table = "WEATHER"  # Match exactly with your MySQL table name (case-sensitive)

    def __str__(self):
        return f"{self.city_id} - {self.city} - {self.temperature}°C - {self.weather_description}"

