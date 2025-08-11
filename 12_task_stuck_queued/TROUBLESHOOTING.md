# Troubleshooting: Task Stuck in Queued State
### Common Causes
1. **No Available Worker Slots**
   - Your executor has no free slots (check `parallelism` and `worker_concurrency`).
   - Workers are busy with other tasks.
2. **Pool Limitations**
   - Task assigned to a pool with no available slots.
   - Use `airflow pools list` to verify availability.
3. **Concurrency Restrictions**
   - `max_active_runs_per_dag` or `dag_concurrency` is too low.
   - Increase in `airflow.cfg` or DAG definition.
4. **Scheduler Delay**
   - Scheduler not picking up new tasks promptly.
   - Restart scheduler:  
     ```bash
     airflow scheduler
     ```
5. **Deadlocked Workers**
   - Worker processes hung or deadlocked.
   - Restart workers:
     ```bash
     airflow celery worker --purge
     ```

### Commands to Debug
- Check tasks in queued state:
  ```bash
  airflow tasks list queued_task_example --tree
  ```

### Check worker availability:
```
bash
airflow celery status
```

### Inspect active tasks:
```
bash
airflow celery inspect active
```
### Best Practices
- Monitor with airflow celery flower for queue and worker health.
- Set realistic concurrency and parallelism values.
- Avoid long-running blocking tasks on shared queues.
