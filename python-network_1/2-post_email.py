#!/usr/bin/python3
"""It takes in a url and an email, sends a POST request"""

import urllib.request
import urllib.parse
import sys

if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]
    data_dict = {"email": email}
    data = urllib.parse.urlencode(data_dict).encode("utf-8")
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode("utf-8")
    print(body)
