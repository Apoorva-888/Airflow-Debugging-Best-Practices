from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def fail_remotely():
    # Simulated remote failure due to missing production config
    if not os.getenv("PROD_API_KEY"):
        raise RuntimeError("Remote failure: PROD_API_KEY is missing in environment variables")

with DAG(
    dag_id="task_failure_remote",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    remote_fail_task = PythonOperator(
        task_id="simulate_remote_failure",
        python_callable=fail_remotely
    )

    remote_fail_task
