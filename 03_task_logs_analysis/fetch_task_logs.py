"""
Fetch Airflow task logs using the Airflow REST API.
Requires: Airflow >= 2.x, API authentication enabled.
"""

import requests
import sys
import os

AIRFLOW_API_BASE = os.getenv("AIRFLOW_API_BASE", "http://localhost:8080/api/v1")
DAG_ID = sys.argv[1] if len(sys.argv) > 1 else "example_dag"
RUN_ID = sys.argv[2] if len(sys.argv) > 2 else "manual__2025-08-08T12:00:00+00:00"
TASK_ID = sys.argv[3] if len(sys.argv) > 3 else "example_task"
TRY_NUMBER = sys.argv[4] if len(sys.argv) > 4 else "1"

def fetch_logs():
    url = f"{AIRFLOW_API_BASE}/dags/{DAG_ID}/dagRuns/{RUN_ID}/taskInstances/{TASK_ID}/logs/{TRY_NUMBER}"
    print(f"Fetching logs from: {url}")

    response = requests.get(url, auth=("admin", "admin"))  # Update auth
    if response.status_code == 200:
        print("✅ Logs fetched successfully")
        return response.text
    else:
        print(f"❌ Failed to fetch logs: {response.status_code}")
        sys.exit(1)

if __name__ == "__main__":
    logs = fetch_logs()
    with open("sample_logs/raw_airflow_log.txt", "w") as f:
        f.write(logs)
    print("Logs saved to sample_logs/raw_airflow_log.txt")
