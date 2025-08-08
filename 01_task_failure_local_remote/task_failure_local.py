from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def fail_locally():
    # Simulated local failure due to missing library
    try:
        import non_existent_package  # This package does not exist
    except ImportError as e:
        raise RuntimeError(f"Local environment issue: {str(e)}")

with DAG(
    dag_id="task_failure_local",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    local_fail_task = PythonOperator(
        task_id="simulate_local_failure",
        python_callable=fail_locally
    )

    local_fail_task
