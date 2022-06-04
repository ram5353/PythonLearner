import requests

parameters = {
    "lat": 39.103119,
    "lon": -84.512016,
    "appid": "53b39eaaf34315392f2ede4d02cd2f26",
    "exclude": "current,minutely,daily"
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"][:12]

will_rain = False

for h in hourly_data:
    weather = h["weather"][0]["id"]
    if weather < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")

print(hourly_data)