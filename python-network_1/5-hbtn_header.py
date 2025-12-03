#!/usr/bin/python3
"""It takes in a url, sends an request to the URL and displays X-Request-Id"""

import requests
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]
    r = requests.get(url)
    x_request_id = r.headers.get("X-Request-Id")
    print(x_request_id)
