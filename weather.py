import requests

spot = input("天気を知りたい場所をローマ字で入力してください。(一文字目は大文字で)")



print(requests.get(f"https://wttr.in/{spot}?format=3").text)