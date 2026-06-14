from http.server import BaseHTTPRequestHandler
import json
import os
import requests

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        client_id = os.environ.get('JD_CLIENT_ID')
        client_secret = os.environ.get('JD_CLIENT_SECRET')

        if not client_id or not client_secret:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Environment variables JD_CLIENT_ID or JD_CLIENT_SECRET not set on Vercel.'}).encode())
            return

        payload = {
            'script': data.get('script'),
            'language': data.get('language', 'csharp'),
            'versionIndex': str(data.get('versionIndex', '3')),
            'clientId': client_id,
            'clientSecret': client_secret
        }

        try:
            r = requests.post('https://api.jdoodle.com/v1/execute', json=payload, timeout=20)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(r.text.encode())
        except Exception as e:
            self.send_response(502)
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())
