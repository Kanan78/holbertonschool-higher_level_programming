#!/usr/bin/python3
"""Sends a POST request to search a user and displays the result."""

import sys
import requests

letter = sys.argv[1] if len(sys.argv) > 1 else ""
url = "http://0.0.0.0:5000/search_user"

try:
    response = requests.post(url, data={'q': letter})
    try:
        data = response.json()
        if data:
            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
except requests.RequestException as e:
    print(f"Error connecting to server: {e}")
