#!/usr/bin/python3
import urllib.requests

url = "https://intranet.hbtn.io/status"
with urllib.requests.urlopen(url) as response:
    data = response.read.decode("utf-8")
print(data)
