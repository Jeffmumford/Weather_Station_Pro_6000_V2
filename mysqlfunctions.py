import mysql.connector
from mysql.connector import Error
from variables import *


#Function to connect to MYSQL server
def create_server_connection(host, database, user_name, user_password):
     connection = None
     try:
         connection = mysql.connector.connect(
             host = host,
             database = database,
             user = user_name,
             passwd = user_password
         )
         print("Database connection successful")
     except Error as err:
         print(f"Error: ' {err}'")
    
     return connection


#Function to insert data in to city's database
def insert_into_database(connection, city):

    #create the connection to the database
    cursor = connection.cursor()

    #mysql statement to insert data into table
    insert_statement = f"""INSERT INTO {city.name.lower()} (year, month, day, time, temperature, conditions) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""
    
    #data to insert into database
    data = (city.year, city.month, city.day, city.time, city.current_temp, city.current_conditions)

    #execute the mysql command
    cursor.execute(insert_statement,data)

    #commit the insert
    connection.commit();
    
    #CLOSE THE CONNECTION TO THE SERVER
    connection.close()
    


