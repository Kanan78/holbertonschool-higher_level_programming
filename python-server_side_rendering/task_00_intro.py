#!/usr/bin/python3
"""This module defines the function generate_invitations"""

import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Template isn't a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(x, dict) for x in attendees):
        print("Attendees must be a list of dicts")
        return

    if template.strip() == "":
        print("Template is empty")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated")
        return

    output_dir = "invites"
    os.makedirs(output_dir, exist_ok=True)

    for index, person in enumerate(attendees, start=1):
        filled_text = (
            template
            .replace("{name}", person.get("name", "N/A"))
            .replace("{event_title}", person.get("event_title", "N/A"))
            .replace("{event_date}", person.get("event_date", "N/A"))
            .replace("{event_location}", person.get("event_location", "N/A"))        
            )
        
        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as f:
                f.write(filled_text)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
