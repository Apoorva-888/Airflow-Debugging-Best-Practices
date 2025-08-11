from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def check_data():
    # Simulate S3 check (local file check)
    if not os.path.exists('data/input_data.csv'):
        raise FileNotFoundError("S3 data not found: data/input_data.csv")

def process_data():
    # This will fail if file is missing
    with open('data/input_data.csv', 'r') as f:
        data = f.read()
    print(f"Processing {len(data)} bytes of data...")

default_args = {
    'owner': 'data_engineer',
    'start_date': datetime(2025, 8, 10),
    'retries': 0
}

with DAG(
    's3_data_delay_example',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:

    check_data_task = PythonOperator(
        task_id='check_data_availability',
        python_callable=check_data
    )

    process_data_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data
    )

    check_data_task >> process_data_task
