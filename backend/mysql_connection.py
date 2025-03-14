import mysql.connector

def mysql_connect():
    DB_HOST="127.0.0.1"
    DB_USER="root"
    DB_PASSWORD="root"
    DB_NAME="weather_db"


    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        port=3307,
        password=DB_PASSWORD
    )
    
    cursor = conn.cursor()

    return conn,cursor