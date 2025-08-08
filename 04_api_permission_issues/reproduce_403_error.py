"""
Simulates an API call that results in a 403 Forbidden error.
Replace with your actual endpoint and credentials for testing.
"""

import requests

API_URL = "https://api.example.com/protected-resource"
API_TOKEN = "invalid_or_expired_token"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

try:
    resp = requests.get(API_URL, headers=headers)
    resp.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"❌ HTTP error occurred: {e}")
    print(f"Response status: {resp.status_code}, body: {resp.text}")
