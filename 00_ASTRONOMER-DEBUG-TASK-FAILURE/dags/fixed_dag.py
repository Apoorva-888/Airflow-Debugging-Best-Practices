"""
Fixed DAG version of api_transform_dag demonstrating best practices:
- Fail fast on missing configuration (API_KEY)
- Validate input data before processing
- Raise clear, informative exceptions to aid debugging
- Prevent cascading failures downstream

This DAG fixes the TypeError from the failing version by checking for None
and ensuring 'items' exists before proceeding.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import requests
import logging

log = logging.getLogger("airflow.task")

DEFAULT_ARGS = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=10),
}

def _extract_safe(**context):
    """
    Extract task with fail-fast validation:
    - Checks if API_KEY is set, raises ValueError if not
    - Attempts API call and raises exception on failure (no silent None returns)
    """
    api_key = os.environ.get("API_KEY")
    endpoint = "https://api.example.invalid/data"  # Still fake endpoint for demo

    log.info(f"Starting extract task (safe); endpoint={endpoint}")

    if not api_key:
        # Fail fast with a clear error message
        raise ValueError("API_KEY environment variable is not set. Set API_KEY or use a test stub.")

    try:
        response = requests.get(endpoint, params={"api_key": api_key}, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        log.exception(f"Request to external API failed: {e}")
        raise  # Re-raise to fail the task explicitly

def _transform_safe(**context):
    """
    Transform task with input validation:
    - Pulls data from extract_task via XCom
    - Validates data is not None and contains 'items' key
    - Raises ValueError if validation fails
    """
    ti = context['ti']
    data = ti.xcom_pull(task_ids='extract_task')

    log.info(f"Starting transform task (safe); data={data}")

    if not data or 'items' not in data or not isinstance(data['items'], list):
        raise ValueError("Extracted data missing 'items' list — check extract_task output and API response.")

    num_items = len(data['items'])
    processed = [item for item in data['items'] if item.get('value', 0) > 10]

    log.info(f"Processed {len(processed)} items")
    return {"num_items": num_items, "processed_count": len(processed)}

def _load_safe(result, **context):
    """
    Load task simply logs the processed result.
    """
    log.info(f"Load task received: {result}")

with DAG(
    dag_id="api_transform_dag_fixed",
    default_args=DEFAULT_ARGS,
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["debug-lab"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=_extract_safe,
        provide_context=True,
    )

    transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=_transform_safe,
        provide_context=True,
    )

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=_load_safe,
        op_args=["{{ ti.xcom_pull(task_ids='transform_task') }}"],
        provide_context=True,
    )

    extract_task >> transform_task >> load_task


"""Key fixes & improvements:
extract_task now raises a clear ValueError if API_KEY is missing instead of returning None.
transform_task checks if data and items exist before processing, raising a clear error if not.
This prevents the cryptic TypeError and makes debugging easier by pointing directly to the config problem.
The downstream load task runs only if the upstream tasks succeed, avoiding skipped or inconsistent runs."""
