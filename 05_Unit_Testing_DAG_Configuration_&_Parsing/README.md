# DAG Configuration Tests

This folder contains tests that validate the structure and syntax of Airflow DAGs before they are deployed.

## Purpose

Ensure all DAGs:
- Load without syntax errors
- Contain required tasks

## Files

- `sample_dag.py`  
  A basic ETL DAG used for testing parsing.

- `test_dag_parsing.py`  
  Contains unit tests to validate DAG structure using `pytest`.

- `__init__.py`  
  Python package marker.

## Running Tests

Run the following command from the repo root:

```bash
pytest dag_config_tests/
```
---
##Summary
This structure is great for:
- **CI/CD pipelines** to catch broken DAGs before deployment.
- **Onboarding** new data engineers to understand how a proper DAG is structured.
- Ensuring **basic DAG hygiene**.

