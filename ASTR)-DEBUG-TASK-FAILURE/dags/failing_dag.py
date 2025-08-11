"""
This DAG simulates a common runtime failure scenario:

1. The extract_task tries to call a fake API endpoint with a missing API_KEY environment variable.
2. It returns None due to missing config or request failure.
3. The transform_task expects a valid dict with 'items' key but receives None.
4. This causes a TypeError at runtime (len(None) is invalid).
5. The load_task is skipped since upstream fails.

Purpose:
- Practice debugging runtime errors caused by bad upstream data.
- Explore logs, XComs, and task retry behavior in Airflow.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import requests
import logging

# Get a logger for Airflow task logs
log = logging.getLogger("airflow.task")

# Default task arguments for retries and owner info
DEFAULT_ARGS = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,                  # Retry once on failure
    "retry_delay": timedelta(seconds=10),  # Wait 10 seconds before retry
}

def _extract(**context):
    """
    Extract task:
    - Tries to get an API key from environment variables (API_KEY)
    - Uses a deliberately invalid API endpoint
    - If API_KEY is missing, returns None and logs a warning (simulating misconfiguration)
    - Otherwise tries to call the API (but endpoint is invalid so will raise exception)
    """
    api_key = os.environ.get("API_KEY")  # Intentionally NOT set for failure scenario
    endpoint = "https://api.example.invalid/data"  # Fake endpoint for demo

    log.info(f"Starting extract task; endpoint={endpoint}")

    if not api_key:
        log.warning("API_KEY is not set — returning None to simulate misconfiguration")
        return None

    try:
        response = requests.get(endpoint, params={"api_key": api_key}, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        log.exception(f"Request to external API failed: {e}")
        return None

def _transform(**context):
    """
    Transform task:
    - Pulls data from XCom pushed by extract_task
    - Intentionally assumes data is a dict with key 'items' (list)
    - If data is None, this will raise a TypeError at runtime
    """
    ti = context['ti']
    data = ti.xcom_pull(task_ids='extract_task')

    log.info(f"Starting transform task; data={data}")

    # Intentional bug: if data is None, the next line will raise TypeError
    num_items = len(data['items'])  # This line will fail if data is None

    # Dummy processing logic
    processed = [item for item in data['items'] if item.get('value', 0) > 10]

    log.info(f"Processed {len(processed)} items")
    return {"num_items": num_items, "processed_count": len(processed)}

def _load(result, **context):
    """
    Load task:
    - Receives the processed result from transform task via templated argument
    - Logs the received data
    """
    log.info(f"Load task received: {result}")

# Define the DAG
with DAG(
    dag_id="api_transform_dag",
    default_args=DEFAULT_ARGS,
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["debug-lab"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=_extract,
        provide_context=True,
    )

    transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=_transform,
        provide_context=True,
    )

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=_load,
        # Pull the XCom result from transform_task as a templated argument
        op_args=["{{ ti.xcom_pull(task_ids='transform_task') }}"],
        provide_context=True,
    )

    # Set task dependencies: extract -> transform -> load
    extract_task >> transform_task >> load_task
