import requests
def weather_forecasting():
    api_key = "your_api_key"
    city = input("Enter city: ")
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url).json()
    for forecast in response['list']:
        date = forecast['dt_txt']
        temperature = forecast['main']['temp'] - 273.15
        print(f"{date}: {temperature:.2f}°C")
weather_forecasting()
