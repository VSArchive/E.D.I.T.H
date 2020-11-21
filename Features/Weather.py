import json
import os

import requests
from dotenv import load_dotenv

from Features.Speak import speak

load_dotenv()

LOCATION_API_KEY = os.getenv("LOCATION_API")
WEATHER_API_KEY = os.getenv("WEATHER_API")


# parse weather data
def speak_current_weather(response, city_name):
    if response["cod"] != "404":
        y = response["main"]
        current_temperature = y["temp"]
        weather_response = response["weather"]
        weather_description = weather_response[0]["description"]
        temperature = int(current_temperature) - 273
        text = "Current temperature at " + city_name + " is " + str(
            temperature) + " degrees centigrade " + "and weather is " + weather_description
        print(text)
        speak(text)

    else:
        print("Not Found!!!")


def get_weather_data(city_name):
    weather_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + WEATHER_API_KEY + "&q=" + city_name
    return requests.get(weather_url).json()


# get location data
def get_location():
    location_url = "http://api.ipstack.com/check?access_key=" + LOCATION_API_KEY
    geo_req = requests.get(location_url)
    geo_json = json.loads(geo_req.text)
    return geo_json['city']


def get_weather():
    city_name = get_location()
    speak_current_weather(get_weather_data(city_name), city_name)


def get_weather_at(city_name):
    speak_current_weather(get_weather_data(city_name), city_name)
