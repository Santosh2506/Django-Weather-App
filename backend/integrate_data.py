import fetch_weather
import  create_db
import mysql_connection

conn,cursor=mysql_connection.mysql_connect()


cursor.execute(f"USE weather_db")


for city_info in fetch_weather.weather_data:

    city_id=cursor.lastrowid+1  # for city_id number , displayed in web page .
    #lastrowid is a way to capture the unique id that the database automatically assigns to a new row upon insertion.
    insert_query = f"""
INSERT INTO {create_db.allTables[0]} (city, temperature, weather_description, city_id) 
VALUES(%s, %s, %s, %s);
"""

    cursor.execute(insert_query, (city_info['City'], city_info['Temperature (C)'], city_info['Description'], city_id))

    

    conn.commit()
print("Weather data inserted successfully!")
cursor.close()
