#!/usr/bin/env python3
from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

JD_API = 'https://api.jdoodle.com/v1/execute'

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    return response

@app.route('/api/execute', methods=['POST', 'OPTIONS'])
def execute():
    if request.method == 'OPTIONS':
        return ('', 204)

    data = request.get_json() or {}
    script = data.get('script')
    language = data.get('language', 'csharp')
    versionIndex = data.get('versionIndex', '3')

    client_id = os.environ.get('JD_CLIENT_ID')
    client_secret = os.environ.get('JD_CLIENT_SECRET')

    if not client_id or not client_secret:
        return jsonify({
            'error': 'JDoodle credentials not set. Set JD_CLIENT_ID and JD_CLIENT_SECRET environment variables.'
        }), 400

    payload = {
        'script': script,
        'language': language,
        'versionIndex': str(versionIndex),
        'clientId': client_id,
        'clientSecret': client_secret
    }

    try:
        r = requests.post(JD_API, json=payload, timeout=20)
        r.raise_for_status()
        return jsonify(r.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'proxy error: {str(e)}'}), 502

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
