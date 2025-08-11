# Issue: Task Stuck in Queued State

### Description
A task remains in **queued** state indefinitely, even though:
- The DAG has been parsed successfully.
- The scheduler is running.
- There are no apparent syntax errors.

### Environment

- **Airflow Version**: 2.7.1
- **Executor**: CeleryExecutor
- **Workers**: 2
- **Concurrency Settings**:
  - `parallelism = 2`
  - `dag_concurrency = 1`
  - `max_active_runs_per_dag = 1`
- **Queue**: `default`
- **Python**: 3.10.12

### Steps to Reproduce
1. Deploy DAG `queued_task_example.py` into `dags/` folder.
2. Configure Airflow to use **CeleryExecutor** with only one worker slot.
3. Run a long-running task first to occupy the worker.
4. Trigger `queued_task_example` DAG.
5. Observe that task remains queued until the worker is freed.

### Expected Behavior
Task should start running once a worker slot is available.

### Actual Behavior
Task remains in queued state indefinitely.

### Related Airflow Docs
- [Airflow Concurrency and Parallelism](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/index.html)
- [Airflow Pools](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/pools.html)
