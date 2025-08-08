"""
This test file checks:
Whether the DAG loads correctly.
All tasks are defined.
The DAG is syntactically valid.
Use pytest to run this test.
"""
# test_dag_parsing.py

import pytest
import os
import importlib.util

DAG_PATH = os.path.join(os.path.dirname(__file__), 'sample_dag.py')

def test_dag_file_loads():
    """Test that the DAG file can be imported and parsed without errors."""
    spec = importlib.util.spec_from_file_location("sample_dag", DAG_PATH)
    dag_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dag_module)

    assert hasattr(dag_module, 'dag'), "DAG object not found in the module"
    dag = dag_module.dag

    assert dag.dag_id == 'sample_etl_dag', "DAG ID does not match"
    assert len(dag.tasks) == 3, "Unexpected number of tasks in the DAG"

    task_ids = [task.task_id for task in dag.tasks]
    for expected_task in ['extract', 'transform', 'load']:
        assert expected_task in task_ids, f"Missing task: {expected_task}"
