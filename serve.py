#!/usr/bin/env python3
"""Local preview server that never caches, so edits show up on a plain reload."""
import http.server, socketserver

class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

class Server(socketserver.TCPServer):
    allow_reuse_address = True        # bind straight away after a restart


if __name__ == "__main__":
    with Server(("", 8787), NoCache) as httpd:
        print("serving on http://localhost:8787")
        httpd.serve_forever()
