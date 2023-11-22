import requests
import json
import pyttsx3

while True:
    city = input("Enter the name of City (type 'k' to quit)\n")

    if city.lower() == 'k':
        print("Exiting the program. Goodbye!")

        engine = pyttsx3.init()
        engine.say("Exiting the program. Goodbye!")
        engine.runAndWait()

        break

    url = f"https://api.weatherapi.com/v1/current.json?key=0532ce81cd3f491b91384419232211&q={city}"

    r = requests.get(url)
    wdic = r.json()

    if "current" in wdic and "temp_c" in wdic["current"]:
        w = wdic["current"]["temp_c"]
        condition = wdic["current"]["condition"]["text"]
        wind_speed = wdic["current"]["wind_kph"]
        humidity = wdic["current"]["humidity"]

        print(f"Weather in {city.capitalize()}:")
        print(f"Temperature: {w}°C")
        print(f"Condition: {condition}")
        print(f"Wind Speed: {wind_speed} kph")
        print(f"Humidity: {humidity}%")

        engine = pyttsx3.init()
        engine.say(f"The current temperature in {city} is {w} degrees Celsius with {condition}. "
                   f"The wind speed is {wind_speed} kilometers per hour, and the humidity is {humidity} percent.")
        engine.runAndWait()

    else:
        print("City not found. Please enter a valid city name.")
