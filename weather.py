import requests

# API key
api_key = '0b0475cc4fc9657b20de5cfc183a96fc'
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Prompt user to enter the city name
city_name = input("Enter city name: ")

# Complete URL
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# Get method of requests module to fetch data
response = requests.get(complete_url)

# JSON method of response object
data = response.json()

# Check if city is found
if data["cod"] != "404":
    main = data["main"]
    temperature = main["temp"]
    pressure = main["pressure"]
    humidity = main["humidity"]
    weather = data["weather"]
    weather_description = weather[0]["description"]

    print(f"Temperature: {temperature}")
    print(f"Pressure: {pressure}")
    print(f"Humidity: {humidity}")
    print(f"Weather description: {weather_description}")
else:
    print("City Not Found!")
