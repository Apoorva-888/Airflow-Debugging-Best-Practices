# dag_validation/test_etl_dag_structure.py

from airflow.models.dag import DAG
import importlib.util
import os

def load_dag():
    dag_path = os.path.join(os.path.dirname(__file__), 'sample_etl_dag.py')
    spec = importlib.util.spec_from_file_location("sample_etl_dag", dag_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert hasattr(module, 'dag'), "No DAG found in file"
    dag = module.dag
    assert isinstance(dag, DAG), "Loaded object is not a DAG"
    return dag

def test_dag_id():
    dag = load_dag()
    assert dag.dag_id == 'sample_etl_dag'

def test_task_count():
    dag = load_dag()
    assert len(dag.tasks) == 3

def test_task_dependencies():
    dag = load_dag()
    assert dag.get_task('transform').upstream_task_ids == {'extract'}
    assert dag.get_task('load').upstream_task_ids == {'transform'}
