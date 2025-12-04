#!/usr/bin/python3
"""It defines the functions fetch_and_print_posts and fetch_and_save_posts"""

import requests
import csv


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code == 200:
        print(f"Status Code: {r.status_code}")
        d = r.json()
        for post in d:
            print(post["title"])


def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code == 200:
        ls = []
        d = r.json()
        for post in d:
            ls.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]})

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(l)
