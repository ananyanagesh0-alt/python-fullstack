import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)
data = response.json()
print(data)

import requests

url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)
data = response.json()
print(data)

import requests
api_key = "0c962a94d697c20c6f88c7136f929819"
city=input("Enter the city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
print("status code:", response.status_code)
data = response.json()
if response.status_code == 200:
    print()
    print("Weather information!")
    print("-----------------")
    print("city:", data['name'])
    print("temperature:", data["main"]["temp"], "°C")
    print("humidity:", data["main"]["humidity"], "%")
    print("weather:", data["weather"][0]["description"])
else:
    print("Error:", data["message"])
print(data)

