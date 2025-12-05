#!/usr/bin/python3
"""This module sets up basic web server using the http.server module"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class MyAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        self.wfile.write(b"Hello, this is a simple API!")


server = HTTPServer(("localhost", 8000), MyAPI)

server.serve_forever()
