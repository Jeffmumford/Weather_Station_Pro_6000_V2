import requests 
from variables import *



#function to get API info
def get_weather_data(api_key, city):  
    api_url = "http://api.weatherapi.com/v1/current.json"  
    params = {  
       
        "q": city,
        "key": api_key  
    }  
    response = requests.get(api_url, params=params)  
    data = response.json()  
    return data  

