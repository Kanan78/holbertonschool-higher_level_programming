#!/usr/bin/python3
"""It takes in a URL and an email address, sends a POST request"""

import requests
import sys

if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]
    my_dict = {"email": email}
    r = requests.post(url, data=email)
    print(r.text)
