

from helpers import *
from variables import *
from get_current_weather import *
from mysqlfunctions import *


  
#Create the CurrentWeather class for Guelph
#holds all the weather data
guelph = CurrentWeather(API_KEY,GUELPH)  


#CREATE THE CONNECTION TO THE DATABASE
#needs server IP, database name, username and password imported from variables.py
connection = create_server_connection(HOST, DATABASE, USER, PASSWORD)

#insert weather data into city's database
insert_into_database(connection, guelph)


