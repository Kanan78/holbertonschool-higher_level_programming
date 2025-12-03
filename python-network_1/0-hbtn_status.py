#!/usr/bin/python3
import urllib.request

url = "https://intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    data = response.read().decode("utf-8")
print(data)
