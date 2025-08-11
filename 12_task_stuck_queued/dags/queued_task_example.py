
"""
DAG Name: queued_task_example
Description:
    Simulates an Airflow task that gets stuck in 'queued' state
    when no worker slots are available.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import time

# Dummy function to simulate data extraction
def extract_data(**context):
    """
    Simulates a data extraction job.
    This is intentionally long-running to hold worker slots.
    """
    print("Starting extraction job...")
    time.sleep(300)  # 5 minutes sleep to simulate heavy load
    print("Data extraction complete.")

default_args = {
    'owner': 'data_eng',
    'depends_on_past': False,
    'email': ['alerts@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    'queued_task_example',
    default_args=default_args,
    description='Example DAG to reproduce queued task scenario',
    schedule_interval=None,
    start_date=datetime(2025, 8, 11),
    catchup=False,
    tags=['debug', 'queued', 'scenario12'],
    max_active_runs=1  # Force only one active run
) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
        provide_context=True,
        pool='default',  # Ensure it uses the default pool
    )

    extract_task
