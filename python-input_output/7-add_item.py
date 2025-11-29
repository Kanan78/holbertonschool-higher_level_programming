#!/usr/bin/python3
"""This module adds command-line arguments to a list and save it to a file"""

import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

with open("add_item.json", 'r') as f:
    try:
        current_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        current_list = []

    current_list.extend(sys.argv[1:])
    save_to_json_file(current_list, "add_item.json")
