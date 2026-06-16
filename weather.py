import requests

print(requests.get("https://wttr.in/Tokyo?format=3").text)