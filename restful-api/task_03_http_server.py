#!/usr/bin/python3
"""This module sets up basic web server using the http.server module"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class MyAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

       elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data).encode()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json_data)
            return

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(b'{"status": "OK"}')
            return

        elif self.path == "/info":
            info = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
            }
            payload = json.dumps(info).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(payload)
            return

        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(b'{"error": "Endpoint not found"}')
            return

server = HTTPServer(("localhost", 8000), MyAPI)

server.serve_forever()
