import requests

location = input("Please enter location: ")
params = {"appid": "YOUR_API_KEY_HERE", "q": location, "mode": "json",
          "units": "metric", "lang": "en"}
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather", params)
print(response.text)

json_response = response.json()
print()
print("Temperature: ", json_response["main"]["temp"])
print("Description: ", json_response["weather"][0]["description"])
