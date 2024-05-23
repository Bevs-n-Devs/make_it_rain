# Make It Rain

A simple Flask app that plays the sounds according to user's the local weather.

## Installation
After cloning your repo you will need to create your virtual environment.
```
python -m venv venv
```
Sometimes you may have to use `python3` or `py` depending on which Python version you ahve installed.

## Installing Required Librabies
To do this without any issue, the best thing to do is to install from the `requirements.txt` file. To do this you enter the following in the terminal:
```
pip install -r requirements.txt
```
**Remember to ALWAYS update the `requirements.txt` file after every new import. To do this easily do can enter the following in the terminal:**
```
pip freeze > requirements.txt
```
This will automatically update the `requirements.txt` file with the latest libraries and packages you have downloaded for the app.

## Using The OpenWeather API
The API I used for this application was a free service from [OpenWeather](https://openweathermap.org/), however you will need to [create an account](https://home.openweathermap.org/users/sign_in) in order to get an *API KEY* before using their service. They also have paid services if you would like to refine or cutomise your searches.

If you would like to customise your searches even further, feel free to use other weather tracking APIs, websites such as [Rapid API](https://rapidapi.com/collection/list-of-free-apis) provide some free and paid APIs.

## Run The Application
To run the app simply enter `python main.py` in the terminal.

### Notes
- The logic for getting the location coordinates are not 100% accurate.
- You have to save your own rain sound effect as an `.mp3` and save it in the `assets` folder. Its easy, just download one from Google!
- You can change the length of the sound effect *(in seconds).*
- If the city you have entered is raining, you will hear the sound play first, then the results will load when the sound finishes.
- This is just a quick demonstration with the possibility of expanding.