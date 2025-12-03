#!/usr/bin/python3
"""It takes in a URL, sends a request to the URL and displays the response"""

import requests
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
