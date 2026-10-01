#!/usr/bin/env python3
"""Servidor local para el Atlas de Colonización.

Sirve index.html y reenvía /api/* a https://spansh.co.uk/api/*, así el navegador
no tropieza con restricciones CORS. Solo usa la biblioteca estándar de Python.

Uso:  python server.py   ->  abre http://localhost:8765
"""
import os
import threading
import urllib.error
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 8765
UPSTREAM = "https://spansh.co.uk"
HERE = os.path.dirname(os.path.abspath(__file__))


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _proxy(self):
        length = int(self.headers.get("Content-Length") or 0)
        data = self.rfile.read(length) if length else None
        req = urllib.request.Request(
            UPSTREAM + self.path,
            data=data,
            method=self.command,
            headers={
                "Content-Type": self.headers.get("Content-Type", "application/json"),
                "User-Agent": "AtlasColonizacionPersonal/1.0",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                self._send(r.status, r.read(), r.headers.get("Content-Type", "application/json"))
        except urllib.error.HTTPError as e:
            self._send(e.code, e.read() or b"{}")
        except Exception as e:  # red caída, timeout, etc.
            self._send(502, ('{"error": "%s"}' % str(e).replace('"', "'")).encode())

    def do_GET(self):
        if self.path.startswith("/api/"):
            return self._proxy()
        with open(os.path.join(HERE, "index.html"), "rb") as f:
            self._send(200, f.read(), "text/html; charset=utf-8")

    def do_POST(self):
        if self.path.startswith("/api/"):
            return self._proxy()
        self._send(404, b"{}")

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    url = f"http://localhost:{PORT}"
    print(f"Atlas de Colonización en {url}  (Ctrl+C para salir)")
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
