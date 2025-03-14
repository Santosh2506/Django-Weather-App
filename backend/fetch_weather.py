


import requests
import pandas as pd
import numpy as np 



#API Setup
api_key="89b526cc8c04feee27c2424d11a01239"
city_list = ["New York", "London", "Tokyo", "Paris", "Sydney", "Toronto", "Berlin", "Madrid", "Rome", "Beijing",
    "Moscow", "São Paulo", "Mumbai", "Dubai", "Singapore", "Hong Kong", "Los Angeles", "Chicago", "Seoul", "Istanbul",
    "Bangkok", "Vienna", "Amsterdam", "Lisbon", "Buenos Aires", "Cairo", "Cape Town", "Nairobi", "Jakarta", "Kuala Lumpur",
    "Mexico City", "Caracas", "Lima", "Santiago", "Auckland", "Helsinki", "Oslo", "Stockholm", "Brussels", "Warsaw",
    "Budapest", "Dublin", "Prague", "Copenhagen", "Athens", "Edinburgh", "Zurich", "Geneva", "Doha", "Manila",
    "Riyadh", "Tehran"
]

weather_data=[]

for city in city_list:
    url="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,api_key)




    #To fetch data from API
    response=requests.get(url)
    # if city is found then response will be code : 200
    #response.json() converts the response into dict type
    if response.status_code==200:
        data=response.json()




        #To extract needed relevant data from response
        temperature_kelvin=data['main']['temp']
        temperature_celsius=round(temperature_kelvin-273.15,2)
        #print(temperature_kelvin,temperature_celsius)
        weather_desc=data['weather'][0]['description']
        #print(weather_desc)

        weather_data.append({
            'City':city,
            'Temperature (C)':temperature_celsius,
            'Description':weather_desc
        })

    else:
        print(f"Failed to fetch data for city {city}")

df=pd.DataFrame(weather_data)
for i in weather_data:
    print(i['City'])
print(df)





