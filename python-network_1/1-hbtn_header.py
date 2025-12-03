#!/usr/bin/python3

import sys
import urllib.request

if len(sys.argv) == 2:
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader("X-Request-Id")
    print(x_request_id)
