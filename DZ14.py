import requests
import json
import csv

with open('data2.csv', newline='') as f:
   data = csv.reader(f, delimiter=';')
   for row in data:
      print(', '.join(row))
