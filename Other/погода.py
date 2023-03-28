import requests
from pprint import pprint

appip = 'badc712c407ebf2854bd3f9bd1a05873'
lang = 'ru'  # указываем на каком языке будет выводиться текст ответа
city = input("Введите город:")
country = input("Введите страну :")
URL = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&appid={appip}&lang{lang}'
r = requests.get(f"{URL}{city},{country}&appid={appip}&lang{lang}")
res = r.json()
pprint(res)
