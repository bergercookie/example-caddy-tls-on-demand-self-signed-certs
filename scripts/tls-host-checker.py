#!/usr/bin/env python3

"""
Minimal server that always responds with 200 OK, regardless of the request.

Use it in conjunction with Caddy's On-demand TLS issuance so that caddy is happy
with issuing self-signed certificates regardless of the domain name or IP
address requested by the user.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer


class AlwaysOkHandler(BaseHTTPRequestHandler):
    """HTP Handler that always sends 200 OK, regardless of the request."""

    def do_GET(self):
        """Handle GET requests by always responding with 200 OK."""
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Authorized")

    def log_message(self, format, *args):
        print(f"Checking domain: {self.path}")


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 9000), AlwaysOkHandler)
    server.serve_forever()
