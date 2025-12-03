#!/usr/bin/python3
"""It takes in a url, sends a request to the url and displays the response"""

import urllib.request
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode("utf-8")
            print(data)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
