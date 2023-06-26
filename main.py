import requests
import json
import win32com.client as wincom

city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=4c1133d3bd974980bda113258232606&q={city}"

r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

speak = wincom.Dispatch("SAPI.SpVoice")
text = f"say 'The current weather in {city} is {w} degrees'"
speak.Speak(text)