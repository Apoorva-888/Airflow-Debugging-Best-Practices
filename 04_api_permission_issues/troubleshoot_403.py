"""
Verifies Airflow connection credentials and tests API access.
"""

from airflow.hooks.base import BaseHook
import requests

CONN_ID = "my_api_connection"

def test_api_connection():
    conn = BaseHook.get_connection(CONN_ID)
    token = conn.password  # Assuming token stored as password
    api_url = f"{conn.host}/protected-resource"

    headers = {"Authorization": f"Bearer {token}"}

    resp = requests.get(api_url, headers=headers)
    if resp.status_code == 200:
        print("✅ API access successful")
    elif resp.status_code == 403:
        print("❌ API access forbidden. Check permissions.")
    else:
        print(f"⚠️ Unexpected status: {resp.status_code}")

if __name__ == "__main__":
    test_api_connection()
