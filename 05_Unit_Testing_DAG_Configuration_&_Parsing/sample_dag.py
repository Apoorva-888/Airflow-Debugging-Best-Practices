# A minimal DAG that could represent a basic ETL job for a data engineer. This is useful as a unit-test-safe DAG for parsing tests.

# dag_config_tests/sample_dag.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    print("Extracting data...")

def transform():
    print("Transforming data...")

def load():
    print("Loading data...")

default_args = {
    'owner': 'data_engineer',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='sample_etl_dag',
    default_args=default_args,
    description='A simple ETL DAG for testing purposes',
    schedule_interval='@daily',
    catchup=False,
    tags=['example', 'etl'],
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load,
    )

    extract_task >> transform_task >> load_task
