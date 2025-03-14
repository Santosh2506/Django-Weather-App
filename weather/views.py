import requests
from django.shortcuts import render

# OpenWeatherMap API Key (Replace with your actual API key)
API_KEY = "89b526cc8c04feee27c2424d11a01239"

def home(request):
    weather_data = None  # Default: No data

    if request.method == "POST":
        city = request.POST["city"]
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(api_url)
        if response.status_code == 200:  # Successful API response
            data = response.json()
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "weather_description": data["weather"][0]["description"],
            }
        else:
            weather_data = {"error": "City not found!"}

    return render(request, "weather/home.html", {"weather_data": weather_data})
