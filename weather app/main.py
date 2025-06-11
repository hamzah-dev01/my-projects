import requests
import json

city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=8687406dae6247b28be161330251106&q={city}"

r = requests.get(url)

# checks if the request was successful
if r.status_code == 200:
    wdic = json.loads(r.text)
    print(f"Current temperature in {city}: {wdic['current']['temp_c']}°C")
else:
    print(f"Error fetching weather data. Status code: {r.status_code}")
    print(r.text)  # This will show the error message from the API
    