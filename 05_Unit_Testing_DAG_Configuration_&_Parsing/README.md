# Unit Testing DAG Configuration & Parsing

This module focuses on **validating Airflow DAG syntax** and **ensuring correct DAG loading** without actually running tasks.

## Contents
- `sample_dag.py` — A minimal example DAG for testing.
- `test_dag_parsing.py` — Unit test that:
  - Imports the DAG.
  - Ensures it is a valid Airflow `DAG` object.
  - Checks that tasks and dependencies are defined correctly.

## How to Run
```bash
pytest dag_config_tests/ --disable-warnings -v
```
## Expected Outcome
✅ Test passes if:
- The DAG can be parsed successfully.
- The task IDs are as expected.
- No syntax or import errors occur.
