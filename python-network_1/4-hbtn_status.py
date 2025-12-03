#!/usr/bin/python3
"""It fetches https://intranet.hbtn.io/status"""
import requests

r = requests.get("https://intranet.hbtn.io/status")
print(f"\t- type: {type(r.text)}")
print(f"\t- content: {r.content}")
