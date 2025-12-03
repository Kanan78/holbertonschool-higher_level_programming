#!/usr/bin/python3
"""It takes your GitHub credentials and display your id"""

import requests
import sys

if len(sys.argv) == 3:
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(username, password))
    data = r.json()
    print(data.get("id"))
