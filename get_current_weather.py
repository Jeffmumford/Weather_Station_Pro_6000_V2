from helpers import *
from variables import *

#gathers all data on current weather based on city passed in
class CurrentWeather:
    def __init__(self, api_key, city):
        self.current_weather = get_weather_data(api_key, city)
        self.name = self.current_weather['location']['name']
        self.current_temp = self.current_weather["current"]["temp_c"]
        self.date_time_data = self.current_weather['location']['localtime'].split(" ")
        self.current_date = self.date_time_data[0].split("-")
        self.year = self.current_date[0]
        self.month = self.current_date[1]
        self.day = self.current_date[2]
        self.time = self.date_time_data[1]
        self.current_conditions = self.current_weather['current']['condition']['text']
      
    
    #print out all weather data
    def print_weather(self):
        print(self.current_weather)
    #prints current temp
    def print_temp(self):
        print(self.current_temp)
    #prints current date and time
    def print_date_time(self):
        print(self.current_date)
        print(self.time)
    #print the current condition
    def print_conditions(self):
        print(self.current_conditions)
  


