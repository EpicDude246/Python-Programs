from pprint import pprint
from playsound import playsound
import requests
import win32com.client as wincl
import datetime
import time

speak = wincl.Dispatch("SAPI.SpVoice")
time1 = datetime.datetime.today()
settings = {"Weather": True, "Time": True, "Ints": 1, "Place": "Redmond",
            "AlarmTimes": ['9:20', '9:50', '11:00', '14:30', '15:35', "18:17"]}
while True:
    #speak.Speak("Please input the place.")
    #place = input("Place? ")
    place = settings["Place"]
    # try:
    r = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={place}&APPID=795cdffcd53383a6b29da83e6910d95b')
    # pprint(r.json())
    weatherr = r.json()
    feelslike = round(int(weatherr['main']['feels_like']) * 1.8 - 459.67, 2)
    humidity = weatherr['main']['humidity']
    temp = round(int(weatherr['main']['temp']) * 1.8 - 459.67, 2)
    temp_max = round(int(weatherr['main']['temp_max']) * 1.8 - 459.67, 2)
    temp_min = round(int(weatherr['main']['temp_min']) * 1.8 - 459.67, 2)
    description = weatherr['weather'][0]['description'].lower()
    mainw = weatherr['weather'][0]['main'].lower()
    country = weatherr['sys']['country']
    windspeed = weatherr['wind']['speed']
    placename = weatherr['name']
    weath = f"""
    The weather in {placename}, {country}:
    The weather is \'{mainw}\'.
    The temprature is {temp}.
    The temprature feels like {feelslike}.
    The maximum temprature is {temp_max}, while the minimum temprature is {temp_min}.
    The wind speed is {windspeed}.
    The humidity is {humidity}.
    """
    # print(weath)
    time_delta = (datetime.datetime.today() - time1)
    if time_delta.total_seconds() >= 1*settings["Ints"]:
        if settings["Time"]:
            t = time.localtime()
            current_time = time.strftime("%H:%M", t)
            current_time = current_time.replace(":", " ").replace(
                '00', "O' clock").replace("0", "O")
            speak.Speak("The current time is"+current_time+".")
        if settings["Weather"]:
            speak.Speak(weath)
        time1 = datetime.datetime.today()
    if time.strftime("%H:%M", time.localtime()) in settings["AlarmTimes"]:
        for x in range(20):
            playsound(r"C:\Users\rjajoo\Desktop\Python\Weather\AlarmTone.wav")
    # except:
        #print("This is not a place.")
        #speak.Speak("This is not a place.")
        # continue
