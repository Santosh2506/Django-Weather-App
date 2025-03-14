import mysql_connection


conn,cursor=mysql_connection.mysql_connect()
DB_NAME= str(input("Enter the name of the Database from where the Table to be Truncated : "))
TABLE_NAME=str(input("Enter the name of the Table to be Truncated : "))
 
cursor.execute("USE information_schema ;")

check_existence=f"""
    SELECT IF (EXISTS(
    SELECT 1 FROM information_schema.tables
    WHERE table_schema='{DB_NAME}'
    AND
    table_name='{TABLE_NAME}'),
    'TRUE',
    'FALSE') AS Table_exists
"""


cursor.execute(check_existence)
for result in cursor:
    print(result[0])
    if result[0] == 'TRUE':
        Warn=str(input(f"ARE YOU SURE YOU WANT TO TRUNCATE THE TABLE {TABLE_NAME} FROM DATABASE {DB_NAME}? Y/N " )).upper()

        
        if Warn in ["Y","YES","Yes","yes","y"]:
            cursor.execute(f"USE {DB_NAME}")
            Truncate = f"""
            TRUNCATE TABLE {TABLE_NAME};
            """
            cursor.execute(Truncate)
            print("Truncate Successful")


        elif Warn in ["N","NO","No","no","n"]:
            print("Truncate operation Stopped")

        else:
            print("Provide valid entry")


cursor.close()
conn.close()