import os
from flask import Flask, jsonify
import requests
import pygame
import time
from dotenv import load_dotenv
load_dotenv()



app = Flask(__name__)

# get location
def get_current_location():
    try:
        # Get the IP-based location data from ipinfo.io
        response = requests.get('https://ipinfo.io')
        data = response.json()

        # Extract the location (latitude and longitude)
        location = data['loc']
        latitude, longitude = map(float, location.split(','))

        return latitude, longitude
    except Exception as e:
        print(f"Error getting location: {e}")
        return None, None

# get weather by city
def get_weather_by_city(city_name):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.environ["API_KEY"]}"
    response = requests.get(base_url)
    return response.json()

# get weather by location
def get_weather_by_location(lat, lon):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={os.environ["API_KEY"]}"
    response = requests.get(base_url)
    return response.json()

# rain sound 
def play_rain_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("./assets/soft-rain-ambient.mp3")
    pygame.mixer.music.play()
    time.sleep(10)  # Play for 10 seconds
    pygame.mixer.music.stop()
    


@app.route("/")
def hello_world():
    return "Hello world, hello Yaw!"


@app.route("/ip")
def get_location():
    response = requests.get("https://ipinfo.io")
    data = response.json()

    # get the location
    location = data['loc']
    play_rain_sound()
    return data


# new york, london, manchester, leeds, liverpool
@app.route("/city/<city_name>")
def city_weather(city_name: str):
    weather_data = get_weather_by_city(city_name)
    weather = weather_data['weather'][0]['description']
    if "Rain" in weather_data["weather"][0]["main"]:
        play_rain_sound()
    if "drizzle" in weather:
        play_rain_sound()
    return jsonify({"Weather Results": weather})


@app.route("/location")
def location_weather():
    lat, lon = get_current_location()
    weather_data = get_weather_by_location(lat, lon)
    if "Rain" in weather_data["weather"][0]["main"]:
        play_rain_sound()
    weather = weather_data['weather'][0]['description']
    return jsonify({"Weather Results": weather})




if __name__ == "__main__":
    app.run(
        debug=True
    )