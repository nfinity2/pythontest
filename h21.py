import requests

# API võtme ja linna nime määramine
city = input("Lisa otsistav asukoht: ")
city = city.strip().capitalize()
print("otsitab linn", city)
api_key = "a3d9602676078738af8c318269b011b9"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
print(url)
# API päringu tegemine
response = requests.get(url)

# Vastuse kontrollimine
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Ilma kirjeldus: {weather}")
    print(f"Temperatuur: {temperature} °C")
else:
    print("Viga andmete allalaadimisel:", response.status_code) 