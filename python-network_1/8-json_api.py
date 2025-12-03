#!/usr/bin/python3
"""It takes in a letter and sends a post request with the letter as a parameter"""

import requests
import sys

url = "http://0.0.0.0:5000/search_user"
if len(sys.argv) == 2:
    letter = sys.argv[1]
else:
    letter = ""
data = {"q": letter}
r = requests.post(url, data=data)
try:
    d = r.json()
    if not d:
        print("No result")
    else:
        print(f'[{d.get("id")}] {d.get("name")}')
except json.JSONDecodeError:
    print("Not a valid JSON")
