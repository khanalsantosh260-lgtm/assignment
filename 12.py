#1
import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
print(response.json()["value"])

#2
import requests

city = input("Enter municipality name: ")
api_key = "YOUR_API_KEY"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

data = requests.get(url).json()

if data.get("cod") != 200:
    print("Error:", data.get("message"))
else:
    temp = data["main"]["temp"] - 273.15
    weather = data["weather"][0]["description"]

    print("Weather:", weather)
    print(f"Temperature: {temp:.2f} °C")