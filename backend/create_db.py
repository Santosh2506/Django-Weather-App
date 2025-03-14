# imported module file for connecting mySQL from Docker conatiner
import mysql_connection

"""
This method creates a new cursor object associated with the connection. 
A cursor is used to execute SQL queries and retrieve results from the database.
"""
conn,cursor=mysql_connection.mysql_connect()




cursor.execute(f"USE weather_db")


create_table_query="""
CREATE TABLE  IF NOT EXISTS WEATHER(
        id int AUTO_INCREMENT PRIMARY KEY,
        city VARCHAR(50),
        temperature FLOAT,
        weather_description VARCHAR(100),
        recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        city_id int not null default 0)
"""

cursor.execute(create_table_query)
conn.commit()

cursor.execute("SHOW TABLES")
TABLES = cursor
allTables=[]
for table in TABLES:
    
    allTables.append(table[0])
#print(allTables)
    

cursor.close()



