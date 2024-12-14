import requests
def weather_app(city):
    api_key = "your_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    if response["cod"] == "404":
        print("City not found.")
    else:
        main = response["main"]
        weather = response["weather"][0]["description"]
        print(f"Temperature: {main['temp'] - 273.15}°C")
        print(f"Weather: {weather}")
city = input("Enter city: ")
weather_app(city)
