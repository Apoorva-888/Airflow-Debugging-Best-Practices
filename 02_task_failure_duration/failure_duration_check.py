"""
Check failure duration of a task using Airflow REST API
"""

import requests
from datetime import datetime

BASE_URL = "http://localhost:8080/api/v1"
DAG_ID = "your_dag_id"
TASK_ID = "your_task_id"

# API call to get failed task instances
response = requests.get(
    f"{BASE_URL}/dags/{DAG_ID}/tasks/{TASK_ID}/instances?state=failed"
)
data = response.json()

if data.get("task_instances"):
    first_failure = min([ti["start_date"] for ti in data["task_instances"]])
    last_failure = max([ti["end_date"] for ti in data["task_instances"]])

    # Convert to datetime objects
    first_dt = datetime.fromisoformat(first_failure.replace("Z", "+00:00"))
    last_dt = datetime.fromisoformat(last_failure.replace("Z", "+00:00"))

    duration = last_dt - first_dt

    print(f"Task {TASK_ID} has been failing for: {duration}")
else:
    print(f"No failures found for task {TASK_ID}.")
