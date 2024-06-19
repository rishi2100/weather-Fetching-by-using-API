import requests
import json
import os
city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=1708064eb7db41578f8120059241406&q={city}"
r = requests.get(url)
print("Weather data retrieved successfully!")
#print(r.text)
#print(type(r.text))
dic = json.loads(r.text)
c = (dic["current"]["temp_c"])
print("Weather of "+city+" is",c)
os.system(f"say 'The current weather in {city} is {c} degree celsius' ")
