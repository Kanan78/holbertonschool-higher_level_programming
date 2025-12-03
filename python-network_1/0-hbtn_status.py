#!/usr/bin/python3
import urllib.request

url = "https://intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    data = response.read()
print("Body response:")
print(f"        - type: {type(data)}")
print(f"        - content: {data}")
print(f'        - utf8 content: {data.decode("utf-8")}')
