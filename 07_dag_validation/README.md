# DAG Validation Tests
This folder contains unit tests that validate Airflow DAGs using `airflow.models.DAG`.
## Purpose
Ensure that DAGs:
- Parse correctly
- Contain expected tasks
- Have proper task dependencies
## How to Run
```bash
pytest dag_validation/
```
Sample DAG
sample_etl_dag.py: Simple ETL pipeline
